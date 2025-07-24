import re

def clean_name(nombre_largo):
    """Convierte el nombre largo en un nombre de archivo válido"""
    # Elimina caracteres no alfanuméricos y reemplaza espacios por guiones bajos
    nombre_limpio = re.sub(r"[^\w\s-]", "", nombre_largo).strip().replace(" ", "_")
    return nombre_limpio.lower()
