import threading
import time
from datetime import datetime, timedelta

funciones = {}

def agregar_medicamento(nombre,horas,minutos,dias):
    funciones[nombre] = {"frecuencia":(horas,minutos),"dias":dias,"alarma_activa": True}
    print("medicamento agregado correcta mente")

    def ejecutar_alarma(nombre, horas, minutos, dias):
        for dia in range(dias):
            tiempo = (horas * 3600 + minutos * 60) * (dia + 1)
            time.sleep(tiempo)
            if funciones [nombre]["alarma_activa"]:
                print(f"Hora de tomar el medicamento: {nombre}")
            if dia + 1 == dias:
                print(f"hoy es el ultimo dia del medicamento {nombre}")

    # Crear y comenzar un nuevo hilo para la alarma
    hilo_alarma = threading.Thread(target=ejecutar_alarma, args=(nombre, horas, minutos,dias))
    hilo_alarma.start()
    

def listado_medicamentos():
    print("\n** listado de medicamentos **")
    for nombre, datos in funciones.items():
        print(f"{nombre}, cada {datos['frecuencia'][0]} horas y {datos['frecuencia'][1]} minutos por {datos['dias']} dias")

def medicamento_tomado(nombre):
    if nombre in funciones and dias == 0 :
        funciones[nombre]["alarma_activa"] = False
        print(f"medicamento {nombre} marcado como tomado")
    else :
        print("no se encontro el medicamento en la lista de medicamentos")



while True :
    print("opcion 1: agregar medicamento")
    print("opcion 2: mostrar listado de medicamentos")
    print("opcion 3: eliminar medicamento")
    print("opcion 4: salir")
    op = input("que opcion elije ")
    if op == "1":
        nombre = input("ingrese el medicamento ")
        horas = int(input("ingrese cada cuantas horas debe tomar los medicamentos "))
        minutos = int(input("ingrese los minutos "))
        dias = int(input("ingrese los dias que debe tomar los medicamentos "))
        agregar_medicamento(nombre,horas,minutos,dias)
    
    elif op == "2":
        listado_medicamentos()

    elif op == "3":
        nombre = input("ingrese el nombre del medicamento que ya tomo ")
        medicamento_tomado(nombre)

    elif op == "4":
        break
    else:
        print("no se encontro la opcion que desea realizar")


