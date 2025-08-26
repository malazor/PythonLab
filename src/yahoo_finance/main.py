import yfinance as yf
from src.yahoo_finance.constants import DATE_INTERVAL, MONTH_INTERVAL, WEEK_INTERVAL, DATE5_INTERVAL
import numpy as np
from src.yahoo_finance.utils.tickers.calculations import UtilsCalculations 
import pandas as pd
from time import sleep

symbol = [
    "HG=F"
]

data = yf.download(symbol, start="2021-12-01", end="2025-07-31", interval="1mo", group_by=symbol)

resultados = []

for i in symbol:

    minimo = data[i]["Low"].min()
    maximo = data[i]["High"].max()
    ultimo_precio = data[i]["Close"].iloc[-1]
    ratio = (ultimo_precio-minimo)/(maximo-minimo)

    info = yf.Ticker(i).info

    resultados.append({
#         "Sector": info["sector"],
        "Name": info["shortName"],
        "Ticker": i,
        "Minimo:": minimo,
        "Maximo:": maximo,
        "Ultimo precio": ultimo_precio,
        "Ratio": ratio
    })

    df_results = pd.DataFrame(resultados)
    df_results_050 = df_results[df_results["Ratio"]<0.5].sort_values(by="Ratio", ascending=True)
    df_results_025 = df_results[df_results["Ratio"]<0.25].sort_values(by="Ratio", ascending=True)


    sleep(2)

data.to_csv("cobre.csv", index=True, sep=";")
print (df_results_050)
print (df_results_025)


