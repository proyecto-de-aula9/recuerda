import threading
import time

funciones = {}

def agregar_medicamento(nombre,horas,minutos):
    funciones[nombre] = {"frecuencia":(horas,minutos),"alarma_activa": True}
    print("medicamento agregado correcta mente")

    def ejecutar_alarma(nombre, horas, minutos):
        while True:
            tiempo = horas * 3600 + minutos
            time.sleep(tiempo)
            if funciones [nombre]["alarma_activa"]:
                print(f"Hora de tomar el medicamento: {nombre}")

    # Crear y comenzar un nuevo hilo para la alarma
    hilo_alarma = threading.Thread(target=ejecutar_alarma, args=(nombre, horas, minutos))
    hilo_alarma.start()
    

def listado_medicamentos():
    print("\n** listado de medicamentos **")
    for nombre, datos in funciones.items():
        print(f"{nombre}, cada {datos['frecuencia'][0]} horas y {datos['frecuencia'][1]} minutos")

def medicamento_tomado(nombre):
    if nombre in funciones :
        funciones[nombre]["alarma_activa"] = False
        print(f"medicamento {nombre} marcado como tomado")
    else :
        print("no se encontro el medicamento {nombre} en la lista de medicamentos")



while True :
    print("opcion 1: agregar medicamento")
    print("opcion 2: mostrar listado de medicamentos")
    print("opcion 3: marcar medicamento como tomado")
    print("opcion 4: salir")
    op = input("que opcion elije ")
    if op == "1":
        nombre = input("ingrese el medicamento ")
        horas = int(input("ingrese cada cuantas horas debe tomar los medicamentos "))
        minutos = int(input("ingrese los minutos "))
        agregar_medicamento(nombre,horas,minutos)
    
    elif op == "2":
        listado_medicamentos()

    elif op == "3":
        nombre = input("ingrese el nombre del medicamento que ya tomo ")
        medicamento_tomado(nombre)

    elif op == "4":
        break
    else:
        print("no se encontro la opcion que desea realizar")


