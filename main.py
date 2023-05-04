import time
import csv
import pyautogui
import pyscreeze
import sys

sleep_time = 3

# definir la función buscar_boton
def buscar_boton(ruta_imagen):
    try:
        boton_x, boton_y = pyautogui.locateCenterOnScreen(ruta_imagen)
        pyautogui.click(boton_x, boton_y)
        time.sleep(sleep_time)
    except TypeError:
        print(f"Error: {ruta_imagen}")
        input()
        sys.exit(1)

# pedir numero de la orde

try:
    while True:
    # Pedir al usuario el número de orden
        orden = input("Ingrese el número de orden: ")

        # Verificar si el usuario ingresó un número de orden
        if not orden:
            print("Debe ingresar un número de orden.")
            time.sleep(1)
            continue

        # Preguntar al usuario si el número de orden es correcto
        respuesta = input(f"Ingresó el número de orden {orden}. ¿Es correcto? (s/n): ")

        # Verificar la respuesta del usuario
        if respuesta.lower() == 's':
            # Si la respuesta es sí, salir del ciclo while
            print("Dirijase al sistema anduin, en 5 segundos inicia la automatizacion")
            time.sleep(6)
            break
        elif respuesta.lower() == 'n':
            # Si la respuesta es no, continuar con el ciclo while
            continue
        else:
            # Si la respuesta no es válida, pedir que ingrese una respuesta válida
            print("Debe ingresar 's' o 'n', ahora repita el proceso")
            continue
except Exception as e:
    # Capturamos la excepción y la mostramos
    print("Error: ", e)
    input("Presione enter para salir")
    sys.exit(1)

# Abrir el archivo CSV
with open('datos.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)

    # Recorrer la columna del archivo CSV y escribir el primer dato encontrado
    try: 
        for fila in lector_csv:
            codigo_cable = fila[0]

            #login
            buscar_boton('botones/boton1.JPG')
            
            #escribir el codigo del cable
            pyautogui.typewrite(codigo_cable)
            pyautogui.press('enter')
            time.sleep(sleep_time)

            #da clic al boton de linkear
            buscar_boton('botones/boton2.JPG')

            #da clic al boton cuando pregunsta si desea linkear
            pyautogui.press('enter')
            time.sleep(4)

            #introduce el numero de orden
            pyautogui.typewrite(orden)
            pyautogui.press('enter')
            time.sleep(3)

            #enter a la ventana emergente de que se agrego correctamente
            pyautogui.press('enter')

            #da clic al boton logof
            buscar_boton('botones/logof.JPG')

            #repite el ciclo
            print('cable ', codigo_cable, ' agregado')
    
    except Exception as e:
        # Capturamos la excepción y la mostramos
        print("Error: ", e)
        input()

print("El script ha finalizado. Presione Enter para salir.")
input()
