import time
import csv
import pyautogui
import sys
import os
from colorama import init, Fore, Style


# falta validar que el numero de orden no tenga espacios en blanco ni este en blanco

# def validar_orden(orden):
#     if len(orden) == 0:
#         print(Fore.RED + "Debe ingresar un orden valido. Inténtelo de nuevo." + Fore.RESET)
#         return False
#     else:
init()
print()
while True:
    try:
        sleep_time = int(input("Digete el tiempo de espera en segundos entre cada paso: "))
        if sleep_time < 2 :
            print(Fore.RED + "Debe ingresar un número mayor a 2. Inténtelo de nuevo." + Fore.RESET)
            continue
        break
    except ValueError:
        print(Fore.RED + "Debe ingresar un número entero. Inténtelo de nuevo." + Fore.RESET)

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

        print(Fore.MAGENTA + "Obtendremos las posiciones de los botones, loguin, linkear y logof en ese respectivo orden" + Fore.RESET)
        print("No necesita dar click en el boton para obtener la posicion, solo manterner el puntero encima del boton mientras termina el conteo regresivo")
        print()

        for i in range(3):
            tiempo = 8
            input(f"Presione enter para obtener la posicion del mouse, tiene {str(tiempo)} segundos para posicionar el mouse")
            contador_regresivo(tiempo)
            posicion_clic = pyautogui.position()
            coordenadas += (posicion_clic,)
            print(f"Se agregó {len(coordenadas)} coordenadas: {posicion_clic}")
            input("Enter para continuar")

        escribir_coordenadas_csv('coordenadas.csv', coordenadas)
        input(Fore.GREEN + "Ingreso de coordenadas finalizada, presione enter para continuar" + Fore.RESET)
        print()
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
            
            respuesta = input(Fore.YELLOW + "¿Es correcto? (s/n):" + Fore.RESET)
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
    while True:
        try:
            print()
            num_codes = int(input("Ingrese la cantidad de cables que desea escanear: "))
            if num_codes < 1:
                print()
                print(Fore.RED + "La cantidad de cables debe ser mayor a cero" + Style.RESET_ALL)
                continue
            break
        except ValueError:
            print(Fore.RED + "Debe ingresar un número entero. Inténtelo de nuevo." + Fore.RESET)
    print()
    codes = set()
    count = 0
    print(Fore.GREEN + "Escanee los cables" + Style.RESET_ALL)
    while len(codes) < num_codes:
        while True:
            code = input()
            if code.strip() == "":
                print(Fore.RED + "No puede estar vacío" + Style.RESET_ALL)
            elif " " in code:
                print(Fore.RED + "No puede contener espacios en blanco" + Style.RESET_ALL)
            else:
                break
        if code not in codes:
            codes.add(code)
            count += 1
            print(Fore.CYAN + f"Escaneando {count}/{num_codes}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "El cable ya está escaneado" + Style.RESET_ALL)

    sorted_codes = sorted(codes)
    print()
    print(Fore.GREEN + "Cables escaneados:" + Fore.RESET)
    for code in sorted_codes:
        print(Fore.MAGENTA + code + Fore.RESET)
    print()
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
            print(Fore.CYAN + f'Cable {numero}/{len(sort_cables)} linkeado'+ Fore.RESET)
    
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

        print(Fore.YELLOW + 'Cierre e inicie sesion en anduin' + Fore.RESET)
        print()
        input("Presione Enter para continuar")
        print()
        print(Fore.YELLOW + 'En 20 segundos iniciará la automatizacion' + Fore.RESET)
        print()
        input("Presione Enter para empezar el linkeo")
        print()
        print(Fore.YELLOW + "*************************************************************")
        print(Fore.YELLOW + "#                                                           #")
        print(Fore.YELLOW + "#               Dirijase a la ventana de Anduin             #")
        print(Fore.YELLOW + "#                                                           #")
        print(Fore.YELLOW + "*************************************************************")
        print(Style.RESET_ALL)  # Resetear los estilos de color

        contador_regresivo(20)

        automation(coordenadas, orden, cables)
        
        print()
        print(Fore.GREEN + "#######################################################")
        print(Fore.GREEN + "#                                                     #")
        print(Fore.GREEN + "#                 ¡¡¡ POLLO COMPLETADO  !!!           #")
        print(Fore.GREEN + "#                                                     #")
        print(Fore.GREEN + "#######################################################")
        print(Style.RESET_ALL)  # Resetear los estilos de color
        input("Presione Enter para escanear más cables")
        print()

# iniciar el programa

start()