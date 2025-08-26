import pandas as pd

try:
    # Lectura del archivo CSV
    df = pd.read_csv('src/Pandas/rate_10y.csv', sep=";")

    # Conversion tipo de dato date
    df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

    # Conversion a tipo de dato numerico
    df['rate_10y'] = pd.to_numeric(df['rate_10y'], errors='coerce')

    # Se calcula el promedio por mes y se agrupa por mes
    df_mensual = df.groupby(df['date'].dt.to_period('M'))['rate_10y'].mean().reset_index()

    # Si quieres que la columna sea fecha en formato mes-año (por ejemplo 2025-08-01):
    df_mensual['date'] = df_mensual['date'].dt.to_timestamp()

    print(df_mensual)
except Exception as e:
    print(e)

