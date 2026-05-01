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


def registrar():
    servicios = cargar()

    paquete_fotografico = input("- Nombre del paquete fotográfico: ")
    precio = input("- Precio: $ ")
    tipo_de_evento = input("- Tipo de evento (boda, retrato, producto, etc.): ")
    duracion = input("- Duración estimada (en horas): ")

    servicio = {
        "paquete": paquete_fotografico,
        "precio": precio,
        "evento": tipo_de_evento,
        "duracion": duracion
    }

    servicios.append(servicio)
    guardar(servicios)

    print("- Servicio registrado.")