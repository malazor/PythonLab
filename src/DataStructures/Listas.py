# Crear una lista
frutas = ["manzana", "plátano", "cereza"]
print("Lista inicial:", frutas)

# Acceder a un elemento por su índice (índices empiezan desde 0)
print("Primer fruta:", frutas[0])  # manzana
print("Última fruta:", frutas[-1])  # cereza

# Cambiar un elemento de la lista
frutas[1] = "kiwi"
print("Lista después de cambiar 'plátano' por 'kiwi':", frutas)

# Agregar elementos a la lista
frutas.append("mango")  # Agrega un elemento al final
print("Lista después de agregar mango:", frutas)

# Insertar un elemento en una posición específica
frutas.insert(1, "pera")  # Inserta "pera" en la posición 1
print("Lista después de insertar pera en la posición 1:", frutas)

# Eliminar un elemento por su valor
frutas.remove("cereza")  # Elimina el primer "cereza" encontrado
print("Lista después de eliminar cereza:", frutas)

# Eliminar un elemento por su índice
del frutas[0]  # Elimina el primer elemento (manzana)
print("Lista después de eliminar el primer elemento:", frutas)

# Obtener la longitud de la lista
tamaño_lista = len(frutas)
print("La lista tiene", tamaño_lista, "elementos.")

# Verificar si un elemento está en la lista
existe_platano = "plátano" in frutas
print("¿Está el plátano en la lista?", existe_platano)

# Iterar sobre la lista (recorrerla)
print("\nRecorriendo la lista:")
for fruta in frutas:
    print(fruta)
