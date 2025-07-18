import pandas as pd

def getTipo(edad):
    if edad<= 17:
        return "ADOLESCENTE"
    if (edad>= 18) & (edad <=25):
        return "JOVEN"
    if (edad>= 26) & (edad <=59):
        return "ADULTO"
    if (edad>= 60) & (edad <=75):
        return "ADULTO MAYOR"
    if (edad>= 76):
        return "ANCIANO"
    

try:
    # Lectura del archivo CSV
    df = pd.read_csv('Pandas/Personas_1.csv', sep=";")

    df["Tipo"] = df["Edad"].apply(getTipo)

    df.to_csv('Pandas/personas.csv', sep="|", index=False)
except Exception as e:
    print(e)