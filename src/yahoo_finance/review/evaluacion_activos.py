import yfinance as yf
import pandas as pd
import numpy as np

def hr(titulo, ancho=50, caracter='-'):
    titulo = f' {titulo} '
    print("\n",titulo.center(ancho, caracter),"\n")


# Paso 1: Definir los activos del portafolio
activos = ["QQQ", "^NDX"]

RF = 4.5

# Paso 2: Descargar los datos desde el 01/01/2000 hasta hoy
# datos es un DataFrame
datos = yf.download(activos, start="2025-01-01")

# Paso 3: Extraer solo los precios de cierre ajustado
# Esto devuelve un DataFrame con las 3 columnas
precios = datos['Close']
precio_round = precios.round(2)

# Paso 4: Mostrar las primeras filas
# print("\nPrecios ajustados (primeras filas):\n")
# print(precio_round.head())

# Paso 5: Mostrar las últimas filas
# print("\nPrecios ajustados (últimas filas):\n")
# print(precio_round.tail())Q

# Estadísticas
# Calcular retornos simple y logarítmicos
retorno_simple = precios.pct_change() # pct_change() Cambio porcentual entre valores consecutivos
retorno = np.log(precios / precios.shift(1))

# Elimina la primera fila que tiene NaN
retornos = retorno.dropna()

# print("Retorno simple:\n",retorno_simple.head(5))
# print("Retorno logaritmico:\n",retorno.head(5))
print("Retorno logaritmico:\n",retornos.tail(10))

# Estadisticas descriptivas
hr("Estadísticas descriptivas de los retornos diarios",100,"-")
print(retornos.describe().round(6))

# Volatilidad anual
hr("Volatilidad anual",100,"-")
retorno_anual = retornos.mean()*252
volatilidad_anual = retornos.std()*np.sqrt(252)
print("Retorno anual: ",retorno_anual)
print("Volatilidad anual: ",volatilidad_anual)

# Matriz de correlaciones
hr("Matriz de correlaciones",100,"-")
print(retornos.corr().round(10))

# Ratio Sharpe
# Tasa libre de riesgo anual
rf = RF / 100  # convertir de porcentaje a proporción

# Ratio de Sharpe por activo
sharpe_ratio = (retorno_anual - rf) / volatilidad_anual

hr("Ratio de Sharpe (por activo)", 100, "-")
print(sharpe_ratio.round(4))
