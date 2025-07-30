import os
import yfinance as yf
import pandas as pd
from time import sleep
import json
from src.yahoo_finance.utils.utils import clean_name


def update_ticker_dict():
    # Ruta del directorio actual (este script)
    dir_script = os.path.dirname(os.path.abspath(__file__))

    # Ruta del directorio padre (donde está "data")
    parent_dir = os.path.dirname(dir_script)

    # Construye la ruta completa al archivo CSV
    ruta_csv = os.path.join(parent_dir, "tickers.csv")

    # Intenta leer el archivo
    df = pd.read_csv(ruta_csv, sep=";")

    output = {}

    for idx, body in df.iterrows():
        symbol = body["Ticker"]
        ticker = yf.Ticker(symbol)
        info = ticker.info
        output[symbol] = clean_name(info.get("longName",symbol))
        sleep(2)

    data_folder = os.path.join(parent_dir, "data")
    
    with open(os.path.join(data_folder, "symbols_dict.json"), "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    update_ticker_dict()