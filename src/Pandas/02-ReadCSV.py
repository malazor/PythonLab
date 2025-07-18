import pandas as pd

try:
    # Lectura del archivo CSV
    df = pd.read_csv('Pandas/Personas_1.csv', sep=";")

    # Escritura en pantalla del archivo CSV

    # print("Imprimo solo 3 filas con funcion head(3)")
    # print(df.head(3)) 
    # print("-"*50)
    # print("Imprimo solo 2 ultimas filas con funcion Tail(2)")
    # print(df.tail(2))
    print("-"*50)
    print("Imprimo todo con indices")
    print(df.to_string(index=True))
    print("-"*50)
    # print("Imprimo todo sin indices")
    # print(df.to_string(index=False))
except Exception as e:
    print(e)

