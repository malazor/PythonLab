import re
import json
import os

def clean_name(nombre_largo):
    """Convierte el nombre largo en un nombre de archivo válido"""
    # Elimina caracteres no alfanuméricos y reemplaza espacios por guiones bajos
    nombre_limpio = re.sub(r"[^\w\s-]", "", nombre_largo).strip().replace(" ", "_")
    return nombre_limpio.lower()

def load_json(symbol,folder_path):

    # Ruta del directorio que contiene el script
    dir_script = os.path.dirname(os.path.abspath(__file__))

    # Ruta al directorio padre (uno arriba)
    parent_dir = os.path.dirname(dir_script)

    # Se construye la ruta para que este dentro de la carpeta data
    # Ruta de la carpeta "data" al mismo nivel que el script
    data_folder = os.path.join(parent_dir, folder_path)

    # Abrir el archivo y cargarlo como diccionario
    with open(os.path.join(data_folder, f"{clean_name(symbol)}.json"), 'r') as file:
        return json.load(file)
