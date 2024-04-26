import threading
import time

funciones = {}
historial = []

def agregar_medicamento(nombre,horas,dosis,dias):
    funciones[nombre] = {"horas":horas,dosis:dosis,"dias":dias,"alarma_activa": True}
    print("medicamento agregado correcta mente")

    def ejecutar_alarma(nombre,horas,dosis,dias):
        if funciones[nombre]:
            dosis = dosis * dias
        for i in range (dosis):
            contado = i + 1
            tiempo = horas * 3600
            time.sleep(tiempo)
            if funciones [nombre]["alarma_activa"]:
                print(f"Hora de tomar el medicamento {nombre}")
                registrar_historial(nombre)
            if contado == dosis:
                print(f"hoy es el ultimo dia del medicamento {nombre}")

    # Crear y comenzar un nuevo hilo para la alarma
    hilo_alarma = threading.Thread(target=ejecutar_alarma, args=(nombre,horas,dosis,dias))
    hilo_alarma.start()
    

def listado_medicamentos():
    print("\n** lista de medicamentos **")
    for nombre, datos in funciones.items():
        print(f"{nombre}, cada {datos['horas']} horas y por {datos['dias']} dias")

def parar(nombre):
    if nombre in funciones and dosis == 0 :
        funciones[nombre]["alarma_activa"] = False
        
def eliminar(nombre):
    if nombre in funciones :
        del funciones[nombre]
        print(f"el medicamento {nombre} fue eliminado")
    else :
        print("no se encontro el medicamento")

def registrar_historial(nombre):
    historial.append({"nombre":nombre,"horas":time.strftime("%m-%d %H:%M")})

def mostrar_historial():
    print("***historial de medicamentos tomados***")
    for Historial in historial :
        print(f"{Historial['nombre']}: tomado a las {Historial['horas']}")
    

while True :
    print("opcion 1: agregar medicamento")
    print("opcion 2: mostrar listado de medicamentos")
    print("opcion 3: eliminar medicamento")
    print("opcion 4 mostrar historial de medicamentos tomado")
    print("opcion 5: salir")
    op = input("que opcion elije ")
    if op == "1":
        nombre = input("ingrese el medicamento ")
        horas = int(input("ingrese cada cuantas horas debe tomar los medicamentos "))
        dosis = int(input("ingrese su dosis diaria "))
        dias = int(input("ingrese los dias que debe tomar los medicamentos "))
        agregar_medicamento(nombre,horas,dosis,dias)
    
    elif op == "2":
        listado_medicamentos()

    elif op == "3":
        nombre = input("ingrese el nombre del medicamento que desea eliminar ")
        eliminar(nombre)

    elif op == "4":
        mostrar_historial()

    elif op == "5":
        break
    else:
        print("no se encontro la opcion que desea realizar")


