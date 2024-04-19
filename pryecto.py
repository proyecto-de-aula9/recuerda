funciones = {}

def agregar_medicamento(nobre,horario):
    funciones[nombre] = horario
    print("medicamento agregado correcta mente")

def listado_medicamentos():
    print("\n** listado de medicamentos **")
    for nombre, horario in funciones.items():
        print(f"nombre: {nombre}, cada {horario} horas")



while True :
    print("opcion 1: agregar medicamento")
    print("opcion 2: mostrar listado de medicamentos")
    print("opcion 3: historial de medicamentos tomados")
    print("opcion 4: salir")
    op = input("que opcion elije ")
    if op == "1":
        nombre = input("ingrese el medicamento ")
        horario = input("ingrese cada cuantas hora debe tomar el medicamento ")
        agregar_medicamento(nombre,horario)
    
    elif op == "2":
        listado_medicamentos()

    elif op == "4":
        break
    else:
        print("no se encontro la opcion que desea realizar")


