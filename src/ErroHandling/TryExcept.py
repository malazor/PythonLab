import os

def Welcome():
    print("--------------- Welcome to Sample Function ---------------")
def End():
    print("----------------------------------------------------------")

try:
    os.system('cls')
    i = int(input("Ingrese un numero: "))
    j = int(input("Ingrese otro numero: "))

    s = i+j
    r = i-j
    m = i*j
    d = i/j

except TypeError as e:
    print("Error de tipo de dato incorrecto:")
    print(e)
except ZeroDivisionError as e:
    print("División entre 0:")
    print(e)
except Exception as e:
    print("Error no controlado:")
    print(f"El error lanzado ha sido de tipo {type(e).__name__}")
    print(e)
else:
    print(f"El valor {i} ha sido ingresado correctamente. ")
    print(f"La suma es {s}")    
    print(f"La resta es {r}")    
    print(f"La multiplicacion es {m}")    
    print(f"La division es {d}")    
finally:
    End()
