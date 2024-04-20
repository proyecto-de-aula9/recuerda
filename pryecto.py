funciones = {}

import time

def agregar_medicamento(nombre,horas,minutos):
    funciones[nombre] = horas
    print("medicamento agregado correcta mente")
    tiempo = horas *60 *60 + minutos*60
    print(f"la alarma sonara en {horas} horas y {minutos} minutos ")
    time.sleep(tiempo)
    print("hora de los medicamentos")
    

def listado_medicamentos():
    print("\n** listado de medicamentos **")
    #for nombre, horas in funciones.items():
    print(f"{nombre}, cada {horas} horas y {minutos} minutos")



while True :
    print("opcion 1: agregar medicamento")
    print("opcion 2: mostrar listado de medicamentos")
    print("opcion 3: historial de medicamentos tomados")
    print("opcion 4: salir")
    op = input("que opcion elije ")
    if op == "1":
        nombre = input("ingrese el medicamento ")
        horas = int(input("ingrese cada cuantas horas debe tomar los medicamentos "))
        minutos = int(input("ingrese los minutos "))
        agregar_medicamento(nombre,horas,minutos)
    
    elif op == "2":
        listado_medicamentos()

    elif op == "4":
        break
    else:
        print("no se encontro la opcion que desea realizar")


