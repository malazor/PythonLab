import yfinance as yf
import pandas as pd
import numpy as np

# Paso 1: Definir los activos del portafolio
tickers = ["^GSPC", "^NDX", "GC=F"]  # S&P 500, Nasdaq 100, Oro

# Paso 2: Descargar los datos desde el 01/01/2000 hasta hoy
# datos es un DataFrame
datos = yf.download(tickers, start="2000-01-01", group_by="column")

# Paso 3: Extraer solo los precios de cierre ajustado
# Esto devuelve un DataFrame con las 3 columnas
precios = datos['Close']
precio_round = precios.round(2)

# Paso 4: Mostrar las primeras filas
print("\nPrecios ajustados (primeras filas):\n")
print(precio_round.head())

# Paso 5: Mostrar las últimas filas
print("\nPrecios ajustados (últimas filas):\n")
print(precio_round.tail())

# Estadísticas