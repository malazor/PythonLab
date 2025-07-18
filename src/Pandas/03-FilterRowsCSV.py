import pandas as pd

try:
    # Lectura del archivo CSV
    df = pd.read_csv('Pandas/Personas_1.csv', sep="|")

    print("-"*50)
    print("Selecciono muestra de la columna ID")
    print("-"*50)
    print(df["ID"].tail(5))

    print("-"*50)
    print("Selecciono dos columnas, ID y Nombre")
    print("-"*50)
    print(df[["ID","Nombre"]].tail(5))

    print("-"*50)
    print("Agrego columna calculada Mayor de edad")
    print("-"*50)
    df["Mayor de edad"] = df["Edad"] > 18
    print(df.tail(5))

    print("-"*50)
    print("Filtro filas de acuerdo a un criterio. Muestra menores de 30 años y mayores de 25.")
    print("-"*50)
    print(df[(df["Edad"]<30) & (df["Edad"]> 25)].tail(5))

    # print(df["ID"].to_string(index=True))
except Exception as e:
    print(e)