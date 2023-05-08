import time
import csv
import pyautogui
import sys
import os

sleep_time = int(input("Digete en segundos el tiempo de espera en cada iteracion: "))

# verificar coordenadas
# si están procedo automatizacion, tienen que ser mayor que cero e igual a 3 creo
# sino inicio configuracion
# pido coordenadas

def pedirCoordenadas():
    try:
        coordenadas = tuple()

        for i in range(3):
            contador_regresivo(7)
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

def contador_regresivo(tiempo):
    input(f"Presione enter para obtener la posicion del mouse, tiene {str(tiempo)} segundos para posicionar el mouse")
    inicio = time.time()
    tiempo_transcurrido = 0
    while tiempo_transcurrido < tiempo:
        tiempo_restante = tiempo - tiempo_transcurrido
        print(f"Tiempo restante: {tiempo_restante} segundos", end="\r")
        time.sleep(1)
        tiempo_transcurrido = int(time.time() - inicio)
    print("Tiempo terminado!")

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
                break
            else:
                continue

        return orden
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
                time.sleep(sleep_time)
                
                #escribir el codigo del cable
                pyautogui.write(codigo_cable)
                pyautogui.press('enter')
                time.sleep(sleep_time)

                #da clic al boton de linkear
                x, y = coordenadas[1]
                pyautogui.click(x, y)
                time.sleep(sleep_time)

                #da clic al boton cuando pregunsta si desea linkear
                pyautogui.press('enter')
                time.sleep(sleep_time)

                #introduce el numero de orden
                pyautogui.typewrite(orden)
                pyautogui.press('enter')
                time.sleep(sleep_time)

                #enter a la ventana emergente de que se agrego correctamente
                pyautogui.press('enter')

                #da clic al boton logof
                x, y = coordenadas[2]
                pyautogui.click(x, y)

                #repite el ciclo
                print('cable ', codigo_cable, ' agregado')
                time.sleep(sleep_time)
        
        except Exception as e:
            # Capturamos la excepción y la mostramos
            print("Error: ", e)
            input("Presione enter para salir")

def start():
    coordenadas = leer_coordenadas_csv('coordenadas.csv')
    
    if len(coordenadas) < 3:
        coordenadas = pedirCoordenadas()

    orden = pedirOrden()

    data_csv(coordenadas, orden)

# iniciar el programa
start()
    
input("La automatización ha finalizado. Presione Enter para salir")