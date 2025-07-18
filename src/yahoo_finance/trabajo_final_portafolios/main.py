import pandas as pd
import numpy as np

# Leer archivo
df = pd.read_excel("Datos trabajo.xlsx")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Supongamos tasa libre de riesgo anual
rf_anual = 0.045  # 4.5%
rf_mensual = rf_anual / 12

# --- Retornos ---
# Retornos simples
retornos_simples = df.pct_change().dropna()

# Retornos logarítmicos
retornos_log = np.log(df / df.shift(1)).dropna()

# --- Estadísticas: Retornos Simples ---
media_mensual_s = np.mean(retornos_simples, axis=0)
volatilidad_mensual_s = np.std(retornos_simples, axis=0, ddof=1)

media_anual_s = media_mensual_s * 12
volatilidad_anual_s = volatilidad_mensual_s * np.sqrt(12)
sharpe_rf_s = (media_anual_s - rf_anual) / volatilidad_anual_s

# --- Estadísticas: Retornos Logarítmicos ---
media_mensual_l = np.mean(retornos_log, axis=0)
volatilidad_mensual_l = np.std(retornos_log, axis=0, ddof=1)

media_anual_l = media_mensual_l * 12
volatilidad_anual_l = volatilidad_mensual_l * np.sqrt(12)
sharpe_rf_l = (media_anual_l - rf_anual) / volatilidad_anual_l

# --- Armar tablas ---
estadisticas_simples = pd.DataFrame({
    'Media mensual': media_mensual_s,
    'Volatilidad mensual': volatilidad_mensual_s,
    'Media anual': media_anual_s,
    'Volatilidad anual': volatilidad_anual_s,
    'Sharpe Ratio': sharpe_rf_s
}).round(4)

estadisticas_log = pd.DataFrame({
    'Media mensual': media_mensual_l,
    'Volatilidad mensual': volatilidad_mensual_l,
    'Media anual': media_anual_l,
    'Volatilidad anual': volatilidad_anual_l,
    'Sharpe Ratio': sharpe_rf_l
}).round(4)

# --- Mostrar ---
print("\n📈 Estadísticas con Retornos Simples:\n")
print(estadisticas_simples)

print("\n📉 Estadísticas con Retornos Logarítmicos:\n")
print(estadisticas_log)


# Número de activos
n = retornos_log.shape[1]
pesos = np.full(n, 1/n)  # Vector de pesos iguales

# Nombres de los activos para alinear con columnas
activos = retornos_log.columns
pesos = pd.Series(pesos, index=activos)

# --- Retorno y volatilidad del portafolio ---
# Retornos del portafolio (suma ponderada)
retorno_portafolio_log = retornos_log @ pesos

print("\n💼 Retorno del portafolio mensual:\n")
print(retorno_portafolio_log)

print("\n💼 Media retorno del portafolio anual:\n")
print(retorno_portafolio_log.mean()*12)
media_portafolio_anual = retorno_portafolio_log.mean() * 12
volatilidad_portafolio_anual = retorno_portafolio_log.std(ddof=1) * np.sqrt(12)

# Sharpe del portafolio
sharpe_portafolio = (media_portafolio_anual - rf_anual) / volatilidad_portafolio_anual

# Mostrar resultados
print(f"📌 Estadísticas del portafolio equiponderado:")
print(f"Rendimiento esperado anual: {media_portafolio_anual:.4%}")
print(f"Volatilidad anual: {volatilidad_portafolio_anual:.4%}")
print(f"Sharpe ajustado (rf = 4.5%): {sharpe_portafolio:.4f}")