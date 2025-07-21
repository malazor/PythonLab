import yfinance as yf
import pandas as pd
import numpy as np

# Paso 1: Definir los activos del portafolio
tickers = ["^GSPC", "^NDX", "GC=F"]  # S&P 500, Nasdaq 100, Oro

# Paso 2: Descargar los datos desde el 01/01/2000 hasta hoy
# datos es un DataFrame
datos = yf.download(tickers, start="2007-01-01", group_by="column")

# Paso 3: Extraer solo los precios de cierre ajustado
# Esto devuelve un DataFrame con las 3 columnas
precios = datos['Close']
precio_round = precios.round(2)

# ----------------------------------------------------------------------------------------------
# Calcular retornos simple y logarítmicos
retorno_simple = precios.pct_change()
retorno = np.log(precios / precios.shift(1))

# Elimina la primera fila que tiene NaN
retornos = retorno.dropna()

print("\nSimple:\n", retorno_simple.tail())
print("\nLogarítmico:\n", retorno.tail())

# ----------------------------------------------------------------------------------------------
# Estadisticas descriptivas
print("\nEstadísticas descriptivas de los retornos diarios:\n")
print(retornos.describe().round(6))

# ----------------------------------------------------------------------------------------------
# Promedio y volatilidad anualizados
retorno_anual = retornos.mean() * 252
volatilidad_anual = retornos.std() * np.sqrt(252)

print("\nRetorno promedio anualizado (%):\n")
print((retorno_anual * 100).round(2))

print("\nVolatilidad anualizada (%):\n")
print((volatilidad_anual * 100).round(2))

# ----------------------------------------------------------------------------------------------
# Matriz de correlaciones
print("\nCorrelación entre activos:\n")
print(retornos.corr().round(10))

# ----------------------------------------------------------------------------------------------
# Rendimiento del portafolio
pesos = {"^GSPC":0.3, "^NDX":0.5, "GC=F": 0.2}

# Convertir a Serie con el mismo orden
pesos_serie = pd.Series(pesos)

# Asegurarse que los índices coincidan (opcionalmente ordenar columnas)
retorno_anual = retorno_anual[pesos_serie.index]  # Reordena si hace falta

# Retorno del portafolio: suma ponderada de retornos individuales
retorno_portafolio = (retorno_anual * pesos_serie).sum()

# Mostrar el resultado en porcentaje con 2 decimales
print(f"\n📈 Retorno esperado anual del portafolio: {retorno_portafolio * 100:,.2f}%")

# ----------------------------------------------------------------------------------------------
# Volatilidad del portafolio
cov_diaria = retornos.cov()
cov_anual = cov_diaria * 252

# Asegúrate que el orden de los pesos coincida con el de las columnas
pesos_array = np.array([0.3,0.5,0.2])

# Varianza del portafolio
var_portafolio = np.dot(pesos_array.T, np.dot(cov_anual, pesos_array))

# Desviacion estandar del portafolio
volatilidad_portafolio = np.sqrt(var_portafolio)
print(f"\n📉 Volatilidad anual del portafolio: {volatilidad_portafolio * 100:.2f}%")


# ----------------------------------------------------------------------------------------------
# Ratio sharpe
rf = 0.0447  # 4.47%
sharpe = (retorno_portafolio - rf) / volatilidad_portafolio
print(f"Sharpe Ratio: {sharpe:.2f}")

