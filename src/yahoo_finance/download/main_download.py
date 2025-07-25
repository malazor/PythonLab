import yfinance as yf
import pandas as pd
import numpy as np
import re
import os
from time import sleep
from src.yahoo_finance.utils.utils import clean_name
import argparse
from datetime import datetime

def save_historical_ticker(symbol, start_date, end_date, ticker_interval):
    ticker = yf.Ticker(symbol)

    info = ticker.info

    file_name = info.get("longName",symbol)
    file_name = clean_name(file_name)+"_"+ticker_interval

    data_history = ticker.history(start=start_date, end=end_date, interval=ticker_interval)

    if data_history.empty:
        print("No existe data en el periodo indicado.")
        return
    else:
        # Ruta del directorio que contiene el script
        dir_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta al directorio padre (uno arriba)
        parent_dir = os.path.dirname(dir_script)

        # Se construye la ruta para que este dentro de la carpeta data
        # Ruta de la carpeta "data" al mismo nivel que el script
        data_folder = os.path.join(parent_dir, "data")

        # Crear la carpeta si no existe
        os.makedirs(data_folder, exist_ok=True)

        # Construir rutas completas para los archivos
        csv_path = os.path.join(data_folder, f"{file_name}.csv")
        json_path = os.path.join(data_folder, f"{file_name}.json")

        data_history.to_csv(csv_path)
        # data_history = data_history.reset_index()
        # data_history.to_json(json_path, orient="records", lines=True)

        print(f"✅ Historial de '{file_name}' guardado como:")
        print(f"  - {file_name}.csv")
        # print(f"  - {file_name}.json")

# 🧪 Ejemplo de uso
if __name__ == "__main__":
    # Fecha actual
    today = datetime.today().date()
    one_year_before = today.replace(year=today.year - 1)

    parser = argparse.ArgumentParser(description="Lee y filtra un archivo CSV de datos financieros.")

    parser.add_argument("--symbol", required=True, type=str, help="Símbolo del activo (ej. AAPL)")
    parser.add_argument("--start", type=str, default=str(one_year_before), help="Fecha de inicio (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default=str(today), help="Fecha de fin (YYYY-MM-DD)")
    parser.add_argument("--interval", type=str, default=str("1mo"), help="Puede ser 1mo o 1d")
    args = parser.parse_args()

    save_historical_ticker(args.symbol,args.start, args.end, args.interval)  # Cambia por cualquier símbolo: MSFT, SPY, BTC-USD, etc.
