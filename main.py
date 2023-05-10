import time
import csv
import pyautogui
import sys
import os

sleep_time = int(input("Digete el tiempo de espera en segundo entre cada paso: "))

def contador_regresivo(tiempo):
    inicio = time.time()
    tiempo_transcurrido = 0
    while tiempo_transcurrido < tiempo:
        tiempo_restante = tiempo - tiempo_transcurrido
        print(f"Time: {tiempo_restante} ", end="\r")
        time.sleep(1)
        tiempo_transcurrido = int(time.time() - inicio)

def pedirCoordenadas():
    try:
        coordenadas = tuple()

        for i in range(3):
            tiempo = 8
            input(f"Presione enter para obtener la posicion del mouse, tiene {str(tiempo)} segundos para posicionar el mouse")
            contador_regresivo(tiempo)
            posicion_clic = pyautogui.position()
            coordenadas += (posicion_clic,)
            print(f"Se agregó {len(coordenadas)} coordenadas: {posicion_clic}")
            input("Enter para continuar")

        escribir_coordenadas_csv('coordenadas.csv', coordenadas)
        input("solicitud de coordenadas finalizada, presione enter para continuar")
        return coordenadas
    
    except Exception as e:
        # Capturamos la excepción y la mostramos
        print("Error: ", e)
        input("Presione enter para salir")
        sys.exit(1)

def leer_coordenadas_csv(ruta_archivo):
    coordenadas = ()
    if os.stat(ruta_archivo).st_size == 0:
        return coordenadas
    else:
        with open(ruta_archivo, mode='r') as archivo_csv:
            reader = csv.reader(archivo_csv)
            next(reader)  # saltar la primera fila con los encabezados
            for fila in reader:
                x, y = map(int, fila)
                coordenadas += ((x, y),)
        return coordenadas

def escribir_coordenadas_csv(ruta_archivo, coordenadas):
    with open(ruta_archivo, mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(['x', 'y'])
        for x, y in coordenadas:
            writer.writerow([x, y])

def pedirOrden():
    try:
        while True:
            orden = input("Ingrese el número de orden: ")
            
            if not orden:
                continue
            
            respuesta = input("¿Es correcto? (s/n):")
            if respuesta.lower() == 's':
                return orden
            else:
                continue

    except Exception as e:
        # Capturamos la excepción y la mostramos
        print("Error: ", e)
        input("Presione enter para salir")
        sys.exit(1)

# Abrir el archivo CSV
def data_csv(coordenadas, orden):
    with open('datos.csv', 'r') as archivo:
        lector_csv = csv.reader(archivo)

        # Recorrer la columna del archivo CSV y escribir el primer dato encontrado
        try: 
            for fila in lector_csv:
                codigo_cable = fila[0]

                #login
                x, y = coordenadas[0]
                pyautogui.click(x, y)
                print('logueando')
                contador_regresivo(sleep_time)
                
                #escribir el codigo del cable
                pyautogui.write(codigo_cable)
                pyautogui.press('enter')
                print('Escribiendo el codigo del cable: ', codigo_cable)
                contador_regresivo(sleep_time)

                #da clic al boton de linkear
                x, y = coordenadas[1]
                pyautogui.click(x, y)
                print('Clic boton linkear')
                contador_regresivo(sleep_time)

                #introduce el numero de orden
                pyautogui.typewrite(orden)
                pyautogui.press('enter')
                print('Escribiendo el numero de orden: ', orden)
                contador_regresivo(sleep_time)

                #da clic al boton cuando pregunsta si desea linkear
                pyautogui.press('enter')
                print('Presionando enter')
                contador_regresivo(sleep_time)

                #enter a la ventana emergente de que se agrego correctamente
                pyautogui.press('enter')
                print('Presionando otra vez enter')
                contador_regresivo(sleep_time)

                #da clic al boton logof
                x, y = coordenadas[2]
                pyautogui.click(x, y)
                print('Clic boton logof')
                contador_regresivo(sleep_time)

                #repite el ciclo
                print('cable linkeado')
                print('...')
                print('...')
                print('...')

        
        except Exception as e:
            # Capturamos la excepción y la mostramos
            print("Error: ", e)
            input("Presione enter para salir")

def start():

    coordenadas = leer_coordenadas_csv('coordenadas.csv')

    if len(coordenadas) < 3:
        coordenadas = pedirCoordenadas()

    orden = pedirOrden()
    
    while True:
        print("Empezando automatizacion, de clic en la ventana de anduin")
        contador_regresivo(10)

        data_csv(coordenadas, orden)
        
        input("La automatización ha finalizado. Presione Enter para empezar otra lista de cables.")
        print('...')
        input("Asegurese de borrar la lista del archivo datos.csv y escanear los nuevos cables")

# iniciar el programa
start()
    