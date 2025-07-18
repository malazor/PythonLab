# Crear una tupla
colores = ("rojo", "verde", "azul")

# Acceder a un elemento por su índice (índices empiezan desde 0)
print("Primer color:", colores[0])  # rojo
print("Último color:", colores[-1])  # azul

# Intentar cambiar un valor (esto dará error porque las tuplas son inmutables)
# colores[1] = "amarillo"  # Esto generará un error: TypeError: 'tuple' object does not support item assignment

# Contar cuántas veces aparece un elemento
repeticiones_rojo = colores.count("rojo")
print("El color rojo aparece", repeticiones_rojo, "vez/es en la tupla.")

# Obtener el índice de un elemento
indice_verde = colores.index("verde")
print("El índice de 'verde' es:", indice_verde)

# Longitud de la tupla
tamaño_tupla = len(colores)
print("La tupla tiene", tamaño_tupla, "elementos.")

# Verificar si un elemento está en la tupla
existe_amarillo = "amarillo" in colores
print("¿Está el color amarillo en la tupla?", existe_amarillo)

# Recorrer la tupla
print("\nRecorriendo la tupla:")
for color in colores:
    print(color)
