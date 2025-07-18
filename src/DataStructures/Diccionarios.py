# Crear un diccionario
persona = {
    "nombre": "Juan",
    "edad": 30,
    "altura": 1.75,
    "es_estudiante": True
}

# Acceder a un valor usando su clave
print("Nombre:", persona["nombre"])  # Juan
print("Edad:", persona["edad"])  # 30

# Modificar un valor
persona["edad"] = 31  # Cambiar la edad
print("Edad después de cambio:", persona["edad"])  # 31

# Agregar un nuevo par clave-valor
persona["ciudad"] = "Madrid"
print("Diccionario después de agregar ciudad:", persona)

# Eliminar un par clave-valor
del persona["altura"]  # Eliminar la clave 'altura'
print("Diccionario después de eliminar altura:", persona)

# Verificar si una clave existe
existe_edad = "edad" in persona
print("¿Existe la clave 'edad'?", existe_edad)

# Obtener todas las claves
claves = persona.keys()
print("Claves del diccionario:", claves)

# Obtener todos los valores
valores = persona.values()
print("Valores del diccionario:", valores)

# Recorrer el diccionario
print("\nRecorriendo el diccionario:")
for clave, valor in persona.items():
    print(clave, ":", valor)
