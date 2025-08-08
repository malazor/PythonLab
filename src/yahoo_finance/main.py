import yfinance as yf
from src.yahoo_finance.constants import DATE_INTERVAL, MONTH_INTERVAL, WEEK_INTERVAL, DATE5_INTERVAL
import numpy as np
from src.yahoo_finance.utils.tickers.calculations import UtilsCalculations 
import pandas as pd

symbol = ["UNH"]

data = data = yf.download(symbol, start="2025-06-01", end="2025-08-08", interval="1d", group_by=symbol)

resultados = []

for i in symbol:

    minimo = data[i]["Low"].min()
    maximo = data[i]["High"].max()
    ultimo_precio = data[i]["Close"].iloc[-1]
    ratio = (ultimo_precio-minimo)/(maximo-minimo)

    resultados.append({
        "Ticker": i,
        "Minimo:": minimo,
        "Maximo:": maximo,
        "Ultimo precio": ultimo_precio,
        "Ratio": ratio
    })

    df_results = pd.DataFrame(resultados)
    df_results_050 = df_results[df_results["Ratio"]<0.5].sort_values(by="Ratio", ascending=True)
    df_results_025 = df_results[df_results["Ratio"]<0.25].sort_values(by="Ratio", ascending=True)

print(df_results_050)
print(df_results_025)
