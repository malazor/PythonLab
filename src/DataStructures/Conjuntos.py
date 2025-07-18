# Crear un conjunto
frutas = {"manzana", "plátano", "cereza"}

# Imprimir el conjunto
print("Conjunto de frutas:", frutas)

# Intentar agregar un elemento (conjuntos no permiten elementos duplicados)
frutas.add("kiwi")
print("Conjunto después de agregar kiwi:", frutas)

# Intentar agregar un elemento duplicado (no se agregará)
frutas.add("manzana")
print("Conjunto después de intentar agregar manzana nuevamente:", frutas)

# Eliminar un elemento
frutas.remove("plátano")  # Esto elimina el elemento "plátano"
print("Conjunto después de eliminar plátano:", frutas)

# Eliminar un elemento sin generar error si no existe
frutas.discard("mango")  # Si "mango" no está, no generará error
print("Conjunto después de intentar eliminar mango (no existe):", frutas)

# Verificar si un elemento está en el conjunto
existe_cereza = "cereza" in frutas
print("¿Está la cereza en el conjunto?", existe_cereza)

# Longitud del conjunto
tamaño_conjunto = len(frutas)
print("El conjunto tiene", tamaño_conjunto, "elementos.")

# Recorrer un conjunto
print("\nRecorriendo el conjunto:")
for fruta in frutas:
    print(fruta)

# Operaciones con conjuntos (unión, intersección, diferencia)
otro_conjunto = {"kiwi", "pera", "cereza"}

# Unión
union = frutas.union(otro_conjunto)
print("Unión de conjuntos:", union)

# Intersección
interseccion = frutas.intersection(otro_conjunto)
print("Intersección de conjuntos:", interseccion)

# Diferencia
diferencia = frutas.difference(otro_conjunto)
print("Diferencia de conjuntos:", diferencia)
