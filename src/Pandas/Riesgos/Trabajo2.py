import yfinance as yf
import pandas as pd

# Descargar histórico diario de USDPEN desde Yahoo Finance
ticker = "USDPEN=X"
start_date = "2020-01-01"
end_date = "2025-08-31"

# Bajamos precios diarios
df = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# Nos quedamos solo con el precio de cierre
df = df[["Close"]].dropna()
df.index.name = "Fecha"

# Reamostrar a fin de mes (último día hábil de cada mes)
df_monthly = df.resample("M").last()

# Guardar en CSV
output_file = "USDPEN_cierre_mensual.csv"
df_monthly.to_csv(output_file, index=True, date_format="%Y-%m-%d")

print(f"Archivo CSV generado: {output_file}")
