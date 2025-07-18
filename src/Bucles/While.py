limite = input("Ingrese un numero del 1 al 100: ")

while int(limite)<1 or int(limite)>100:
    limite = input("Rango equivocado, por favor ingresa un numero del 1 al 100:")

print("El numero ingresado es ", limite)