import json
from config import RUTA_SERVICIOS

def cargar():
    try:
        with open(RUTA_SERVICIOS, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar(servicios):
    with open(RUTA_SERVICIOS, "w", encoding="utf-8") as archivo:
        json.dump(servicios, archivo, indent=4, ensure_ascii=False)


def editar_servicio():
    servicios = cargar()

    nombre_buscar = input("Ingrese el nombre del paquete a editar: ")

    for servicio in servicios:
        if servicio["paquete"].lower() == nombre_buscar.lower():

            print("\nDejar vacío si no desea cambiar")

            nuevo_nombre = input(f"Nuevo nombre ({servicio['paquete']}): ")
            nuevo_precio = input(f"Nuevo precio ({servicio['precio']}): ")
            nueva_duracion = input(f"Nueva duración ({servicio['duracion']}): ")

            # Actualizar datos solo si el usuario escribe algo
            if nuevo_nombre:
                servicio["paquete"] = nuevo_nombre

            if nuevo_precio:
                if nuevo_precio.isdigit():
                    servicio["precio"] = nuevo_precio
                else:
                    print("Precio inválido.")
                    return

            if nueva_duracion:
                if nueva_duracion.isdigit():
                    servicio["duracion"] = nueva_duracion
                else:
                    print("Duración inválida.")
                    return

            guardar(servicios)
            print("Servicio editado correctamente.")
            return

    print("Servicio no encontrado.")