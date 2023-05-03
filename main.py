import time
import csv
import pyautogui

# Esperar 5 segundos para que tengas tiempo de abrir la ventana que contiene los botones
time.sleep(5)

# Abrir el archivo CSV que tiene la orden
with open('orden.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)

    # Recorrer la columna del archivo CSV y escribir el primer dato encontrado
    for fila in lector_csv:
        orden = fila[0]
        break

# Abrir el archivo CSV
with open('datos.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)

    # Recorrer la columna del archivo CSV y escribir el primer dato encontrado
    for fila in lector_csv:
        codigo_cable = fila[0]

        #login
        boton1_x, boton1_y = pyautogui.locateCenterOnScreen('botones/boton1.JPG')
        pyautogui.click(boton1_x, boton1_y)
        time.sleep(2)
        
        #escribir el codigo del cable
        pyautogui.typewrite(codigo_cable)
        pyautogui.press('enter')
        time.sleep(3)

        #da clic al boton de linkear
        boton2_x, boton2_y = pyautogui.locateCenterOnScreen('botones/boton2.JPG')
        pyautogui.click(boton2_x, boton2_y)
        time.sleep(2)

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
        boton3_x, boton3_y = pyautogui.locateCenterOnScreen('botones/logof.JPG')
        pyautogui.click(boton3_x, boton3_y)
        time.sleep(2)

        #repite el ciclo
        with open("status.txt", "w") as f:
            f.write("finish")
