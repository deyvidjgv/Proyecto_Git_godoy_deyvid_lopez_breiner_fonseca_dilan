# Proyecto_Git_godoy_deyvid_lopez_breiner_fonseca_dilan
 PhotoCampus


# PhotoCampus - Sistema de Gestión de Servicios Fotográficos

## Introducción

PhotoCampus es un sistema desarrollado en Python que permite gestionar servicios fotográficos desde consola. El programa ofrece funcionalidades para registrar, editar y eliminar paquetes fotográficos, incluyendo información como nombre del paquete, precio, tipo de evento y duración.

El desarrollo del proyecto se realizó utilizando control de versiones con Git, aplicando trabajo por ramas para simular un entorno colaborativo.

---

## Instrucciones para configurar y usar el sistema

### Requisitos

* Python 3 instalado
* Editor de código (se recomienda Visual Studio Code)

### Ejecución

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

2. Ingresar a la carpeta del proyecto:

```bash
cd nombre-del-proyecto
```

3. Ejecutar el programa principal:

```bash
python main.py
```

---

### Uso del sistema

Al ejecutar el programa, se mostrará un menú con las siguientes opciones:

1. Registrar servicios: permite agregar un nuevo paquete fotográfico.
2. Editar servicios: permite modificar un servicio existente.
3. Eliminar servicios: permite eliminar un servicio por nombre.
4. Salir: finaliza el programa.

Los datos se almacenan en un archivo JSON llamado `Ruta_servicios.json`.

---

## Estructura del repositorio

```
proyecto/
│
├── main.py                # Archivo principal con el menú
├── add_services.py        # Función para registrar servicios
├── edit_service.py        # Función para editar servicios
├── eliminar.py            # Función para eliminar servicios
├── config.py              # Configuración de rutas
├── Ruta_servicios.json    # Archivo de almacenamiento de datos
└── README.md              # Documentación del proyecto
```

---

## Flujo de trabajo con Git

El proyecto se desarrolló utilizando un flujo de trabajo basado en ramas:

* main: rama principal del proyecto
* feature-add: desarrollo de la funcionalidad de registro
* feature-edit: desarrollo de la funcionalidad de edición
* feature-delete: desarrollo de la funcionalidad de eliminación

Cada funcionalidad fue desarrollada en su propia rama y posteriormente integrada a la rama principal mediante el uso de merge.

---

## Resolución de conflictos

Durante la integración de ramas se presentó un conflicto al realizar un merge. Esto ocurrió porque dos ramas contenían cambios en las mismas secciones de un archivo, por lo que Git no pudo resolver automáticamente cuál versión conservar.

El editor mostró las opciones para elegir entre los cambios actuales, los cambios entrantes o una combinación de ambos.

### Proceso de resolución

1. Se revisaron los cambios en conflicto dentro del editor.
2. Se compararon ambas versiones del código.
3. Se decidió conservar y combinar manualmente las partes necesarias de cada una.
4. Se eliminaron los marcadores de conflicto generados por Git (`<<<<`, `====`, `>>>>`).
5. Se guardaron los cambios directamente en el archivo.

En este caso, no se realizó el commit inmediatamente después de la resolución debido a un descuido, pero el conflicto fue solucionado correctamente mediante la edición manual del código.

---

## Conclusión

El desarrollo de este proyecto permitió aplicar conceptos fundamentales como la manipulación de archivos JSON, la organización modular en Python y el uso de Git para el control de versiones. Además, se adquirió experiencia en la gestión de ramas y la resolución manual de conflictos durante la integración de funcionalidades.
