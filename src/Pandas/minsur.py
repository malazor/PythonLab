import pandas as pd

# Ruta de tu archivo CSV
archivo = "src/Pandas/v_prices_daily.csv"

# Leer el CSV
df = pd.read_csv(archivo, sep=";")

# Convertir la columna date a datetime
df["date"] = pd.to_datetime(df["date"],format="%d/%m/%Y")

# Asegurarse que los datos estén ordenados
df = df.sort_values(by=["symbol", "date"])

# También puedes crear DataFrames individuales (uno por símbolo)
# df_copa   = df[df["symbol"] == "COPA.L"].copy()
# df_cper   = df[df["symbol"] == "CPER.L"].copy()
df_gold_f = df[(df["symbol"] == "GC=F") & (df["date"] > "2020-01-01")].copy()
# df_gld    = df[df["symbol"] == "GLD"].copy()
df_cu     = df[(df["symbol"] == "HG=F") & (df["date"] > "2020-01-01")].copy()
# df_iau    = df[df["symbol"] == "IAU"].copy()
df_minsur = df[(df["symbol"] == "MINSURI1.LM") & (df["date"] > "2020-01-01")].copy()
# df_tin    = df[df["symbol"] == "TIN"].copy()
# df_tinm   = df[df["symbol"] == "TINM.L"].copy()

df_gold_f = df_gold_f.rename(columns={"ultimo_cierre": "GC=F"})
df_cu     = df_cu.rename(columns={"ultimo_cierre": "HG=F"})
df_minsur = df_minsur.rename(columns={"ultimo_cierre": "MINSURI1.LM"})

df_final = df_gold_f.merge(df_cu, on="date", how="inner") \
                    .merge(df_minsur, on="date", how="inner")


# Agrupar por MINSUR y por mes usando Grouper
estadisticas_minsur = (
    df_minsur.groupby(["symbol", pd.Grouper(key="date", freq="ME")])
    .agg(
        promedio_cierre=("close", "mean"),
        max_cierre=("close", "max"),
        min_cierre=("close", "min"),
        ultimo_cierre=("close", "last"),
    )
    .reset_index()
)

estadisticas_gold = (
    df_gold_f.groupby(["symbol", pd.Grouper(key="date", freq="ME")])
    .agg(
        promedio_cierre=("close", "mean"),
        max_cierre=("close", "max"),
        min_cierre=("close", "min"),
        ultimo_cierre=("close", "last"),
    )
    .reset_index()
)

estadisticas_cu = (
    df_cu.groupby(["symbol", pd.Grouper(key="date", freq="ME")])
    .agg(
        promedio_cierre=("close", "mean"),
        max_cierre=("close", "max"),
        min_cierre=("close", "min"),
        ultimo_cierre=("close", "last"),
    )
    .reset_index()
)
print(df_final)
# Mostrar resultado
estadisticas_minsur.to_csv("estadisticas_minsur.csv", index=False)
# estadisticas_tin.to_csv("estadisticas_tin.csv", index=False)
estadisticas_gold.to_csv("estadisticas_gold.csv", index=False)
estadisticas_cu.to_csv("estadisticas_cu.csv", index=False)
# Guardar en CSV si lo necesitas
# estadisticas.to_csv("estadisticas_mensuales.csv", index=False)
