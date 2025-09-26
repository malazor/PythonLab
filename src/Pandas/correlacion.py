import pandas as pd


# Cargar datos (puede ser Excel o CSV)
df = pd.read_csv("src/Pandas/datos.csv",sep=";")

# Convertir todas las columnas numéricas a float
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce") 

# Matriz de correlación
correlation_matrix = df.corr()

# Matriz corrleación anticipada
corr_anticipadas = df.corrwith(df.shift(-1)["pendiente"])

# Matriz corrleación rezagada
corr_rezagada = df.corrwith(df.shift(+1)["pendiente"])

print(correlation_matrix)

print(corr_anticipadas)
print(corr_rezagada)
