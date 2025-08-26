import pandas as pd

try:
    # Lectura del archivo CSV
    df = pd.read_csv('src/Pandas/curva_soberana.csv', sep=";")

    # Conversion tipo de dato date
    df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

    # Conversion a tipo de dato numerico
    df['tasa'] = pd.to_numeric(df['tasa'], errors='coerce')

    # Se calcula el promedio por mes y se agrupa por mes
    # df_mensual = df.groupby(df['date'].dt.to_period('M'))['rate_3mo'].mean().reset_index()
    df_90 = df[df['plazo'] == 90].groupby(df['date'].dt.to_period('M'))['tasa'].mean().reset_index()

    df_3600 = df[df['plazo'] == 3600].groupby(df['date'].dt.to_period('M'))['tasa'].mean().reset_index()


    # Si quieres que la columna sea fecha en formato mes-año (por ejemplo 2025-08-01):
    df_90['date'] = df_90['date'].dt.to_timestamp()
    df_3600['date'] = df_3600['date'].dt.to_timestamp()

    print("90 dias")
    print("-"*30)
    print(df_90)
    print("-"*30)    
    print("10 años")
    print("-"*30)    
    print(df_3600)
except Exception as e:
    print(e)

