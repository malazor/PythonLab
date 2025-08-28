import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Cargar datos (puede ser Excel o CSV)
df = pd.read_csv("src/Pandas/datos.csv",sep=";")

# Convertir todas las columnas numéricas a float
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce") 

result = adfuller(df["au"].dropna())  # dropna para evitar NaN
print("ADF Statistic:", result[0])
print("p-value:", result[1])
print("Critical Values:", result[4])

# Matriz de correlación
# correlation_matrix = df.corr()

# Matriz corrleación anticipada
# corr_anticipadas = df.corrwith(df.shift(-1)["pendiente"])

# Matriz corrleación rezagada
# corr_rezagada = df.corrwith(df.shift(+1)["pendiente"])

# print(correlation_matrix)

# print(corr_anticipadas)
# print(corr_rezagada)
