import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Cargar datos (puede ser Excel o CSV)
df = pd.read_csv("src/Pandas/datos_d.csv",sep=";")
df_clean = df.dropna()

# Convertir todas las columnas numéricas a float
for col in df_clean.columns:
    df_clean[col] = pd.to_numeric(df_clean[col], errors="coerce") 

# result = adfuller(df["au"].dropna())  # dropna para evitar NaN
# print("ADF Statistic:", result[0])
# print("p-value:", result[1])
# print("Critical Values:", result[4])

# Matriz de correlación
correlation_matrix = df_clean.corr()

# Matriz corrleación anticipada
#corr_anticipadas = df.corrwith(df.shift(-1)["pendiente"])
 
# Matriz corrleación rezagada
#corr_rezagada = df.corrwith(df.shift(+1)["pendiente"])

# print(df.describe())

# print(corr_anticipadas)
# print(corr_rezagada)
X = ['au', 'cu','d_desempleo','d_pbi','embig','tc']
Y = ['pendiente']
K=[1,2,3,4,5,6]

resultados = []

for i in Y:       # variable dependiente
    for j in X:   # variables independientes
        for k in K:   # número de rezagos/adelantos
            # Correlación adelantada (cu en t+k, pendiente en t)
            corr_adelantada = df_clean[i].corr(df_clean.shift(-k)[j])
            
            # Correlación rezagada (cu en t-k, pendiente en t)
            corr_rezagada = df_clean[i].corr(df_clean.shift(k)[j])
            
            # Guardamos los resultados como diccionario
            resultados.append({
                "dependiente": i,
                "independiente": j,
                "k": k,
                "tipo": "adelantada",
                "correlacion": corr_adelantada
            })
            
            resultados.append({
                "dependiente": i,
                "independiente": j,
                "k": k,
                "tipo": "rezagada",
                "correlacion": corr_rezagada
            })

# Convertimos la lista en DataFrame
output = pd.DataFrame(resultados)

# output.to_csv("src/Pandas/correlaciones.csv", index=False, encoding="utf-8")

agrupado = output.groupby("independiente")["correlacion"].agg(["min", "max"])
print(agrupado)
# print(df_clean["pendiente"].corr(df_clean.shift(-1)["cu"]))
# print(correlation_matrix)