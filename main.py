import time
import csv
import pyautogui
import sys
import os
from colorama import init, Fore, Style

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

def scan_codes():
    num_codes = int(input("Ingrese la cantidad de códigos a escanear: "))
    codes = set()
    count = 0
    while len(codes) < num_codes:
        while True:
            code = input("Ingrese el código a escanear: ")
            if code.strip() == "":
                print("No puede estar vacío")
            elif " " in code:
                print("No puede contener espacios en blanco")
            else:
                break
        if code not in codes:
            codes.add(code)
            count += 1
            print(f"Escaneado código {count}/{num_codes}")
        else:
            print("El código ya está escaneado")
    sorted_codes = sorted(codes)
    print("Códigos escaneados:")
    for code in sorted_codes:
        print(code)
    
    return sorted_codes

# Abrir el archivo CSV
def automation(coordenadas, orden, sort_cables):
    try:             
        for i, codigo_cable in enumerate(sort_cables):

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

            #introduce el numero de orden
            pyautogui.typewrite(orden)
            pyautogui.press('enter')
            time.sleep(sleep_time)

            #da clic al boton cuando pregunsta si desea linkear
            pyautogui.press('enter')
            time.sleep(sleep_time)

            #enter a la ventana emergente de que se agrego correctamente
            pyautogui.press('enter')
            time.sleep(sleep_time)

            #da clic al boton logof
            x, y = coordenadas[2]
            pyautogui.click(x, y)
            time.sleep(sleep_time)

            #repite el ciclo
            numero = i + 1
            print(f'Escaneado {numero}/{len(sort_cables)}: {codigo_cable}')
    
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
        cables = scan_codes()
        init()
        print(Fore.YELLOW + 'Cierre e inicie sesion en anduin antes de continuar' + Fore.RESET)
        input('En 10 segundos iniciará la automatizacion, Presione enter para continuar')
        print(Fore.YELLOW + 'Asegurese de posicionarse en la ventana de Anduin' + Fore.RESET)
        contador_regresivo(10)

        automation(coordenadas, orden, cables)
        
        init()  # Inicializar colorama

        print(Fore.GREEN + "##############################")
        print(Fore.GREEN + "#                            #")
        print(Fore.GREEN + "#       TAREA FINALIZADA     #")
        print(Fore.GREEN + "#                            #")
        print(Fore.GREEN + "##############################")
        print(Style.RESET_ALL)  # Resetear los estilos de color
        input("Presione Enter para INGRESAR otra lista de cables")


# iniciar el programa
start()