from edit_service import *
import json
from add_services import *
from eliminar import *

while True:
    print("====================================================")
    print("  Bienvenido PhotoCampus Fotografia profesional")
    print("===================================================")
    print("1. Registrar servicios")
    print("2. Editar servicios")
    print("3. Eliminar servicios")
    print("4. Salir")

    opcion = input("Digite una opción: ")
    print()


    if opcion == "1":
            registrar()

    elif opcion == "2":
            editar_servicio()

    elif opcion == "3":
            eliminar_servicio()

    elif opcion == "4":
        salir = input("¿Quieres salir del programa Si/No: ").capitalize()
        if salir == "Si":
            print("-Saliste del programa...\n")
            break
        elif salir == "No":
            print()
            continue
    else:
        print("-Error: No existe la opción.\n")
