import pandas as pd

    

try:
    # Lectura del archivo CSV
    df = pd.read_csv('Pandas/Personas_1.csv', sep=";")

    print(df.tail(5))
    nuevo = df.drop(columns=["Tipo"])
    print(nuevo.tail(5))


except Exception as e:
    print(e)