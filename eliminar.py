import json

def eliminar_servicio(nombre_servicio, archivo="data.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            servicios = json.load(f)
        nuevos_servicios = [
            servicio for servicio in servicios
            if servicio["nombre"].lower() != nombre_servicio.lower()
        ]
        if len(servicios) == len(nuevos_servicios):
            print("⚠️ Servicio no encontrado.")
            return
        with open(archivo, "w", encoding="utf-8") as f:
            json.dump(nuevos_servicios, f, indent=4, ensure_ascii=False)
        print("Servicio eliminado correctamente.")
    except FileNotFoundError:
        print(" El archivo no existe.")
    except json.JSONDecodeError:
        print(" Error al leer el archivo JSON.")