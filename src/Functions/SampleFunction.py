def Welcome():
    print("--------------- Welcome to Sample Function ---------------")
def End():
    print("----------------------------------------------------------")

def Suma(a=0,b=0):
    return a+b

Welcome()
in1 = int(input("Ingrese un numero: "))
in2 = int(input("Ingrese otro numero: "))

print("La suma es: ", Suma(in1, in2))
End()