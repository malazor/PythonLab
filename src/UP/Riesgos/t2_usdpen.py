import pandas as pd
import numpy as np
import src.UP.Riesgos.utils.utils as utils
import yfinance as yf

SEED = 42
np.random.seed(SEED)

# Descargar histórico diario de USDPEN desde Yahoo Finance
ticker = "USDPEN=X"
start_date = "2021-12-31"
end_date = "2025-08-31"

# Bajamos precios diarios
df = yf.download(ticker, start=start_date, end=end_date, interval="1d")

# Nos quedamos solo con el precio de cierre
df = df[["Close"]].dropna()
df.index.name = "Fecha"

# Reamostrar a fin de mes (último día hábil de cada mes)
df_monthly = df.resample("ME").last()
df_monthly["diff"] = df_monthly["Close"].pct_change()
mean_diff, std_diff = df_monthly["diff"].mean(), df_monthly["diff"].std()

# print(f"Archivo CSV generado: {output_file}")
#print(f"Media: {mean_diff}")
#print(f"Desviacion Std: {std_diff}")

future_dates = pd.date_range(start="2025-09-30", end="2031-12-31", freq="ME")

last_value = float(df_monthly["Close"].iloc[-1])

projections = []
current_value = last_value



for date in future_dates:
    temp = current_value
    shock = np.random.normal(loc=mean_diff, scale=std_diff)  # en %
#    current_value = last_value * (1 + shock/100)
    current_value = last_value * (1 + shock)
    last_diff = (current_value - temp)/current_value
    projections.append((date, current_value, last_diff))

df_future = pd.DataFrame(projections, columns=["Fecha", "Close", "diff"]).set_index("Fecha")

df_extended = pd.concat([df_monthly, df_future])

# Último día de 2026
val_2026 = df_future.loc["2026-12-31", "Close"]

# Último día de 2027
val_2027 = df_future.loc["2027-12-31", "Close"]

# Último día de 2028
val_2028 = df_future.loc["2028-12-31", "Close"]

# Último día de 2029
val_2029 = df_future.loc["2029-12-31", "Close"]

# Último día de 2030
val_2030 = df_future.loc["2030-12-31", "Close"]

# Último día de 2031
val_2031 = df_future.loc["2031-12-31", "Close"]

df_sim = utils.simulacion_tc(df_future, mean_diff, std_diff, SEED)

print(df_sim.mean().to_frame(name="Media"))

# Exportar a CSV
df_sim.to_csv("simulacion_usdpen.csv", index=False)

# Guardar en CSV
output_file = "USDPEN_cierre_mensual_historico.csv"
df_monthly.to_csv(output_file, index=True, date_format="%Y-%m-%d")

# Guardar en CSV Futuros
output_file = "USDPEN_cierre_mensual_futuros.csv"
df_future.to_csv(output_file, index=True, date_format="%Y-%m-%d")

# Guardar en CSV Total
output_file = "USDPEN_cierre_mensual_completo.csv"
df_extended.to_csv(output_file, index=True, date_format="%Y-%m-%d")

# Llamar a la función del módulo
# resultados = utils.analizar_distribucion(df_monthly, col="Close")
# print(resultados)