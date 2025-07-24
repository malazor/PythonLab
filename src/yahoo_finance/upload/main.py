import yfinance as yf
import pandas as pd
import numpy as np
import re
import os
from time import sleep

def save_historical_ticker(symbol, ticker_interval):
    ticker = yf.Ticker(symbol)

    info = ticker.info

    file_name = info.get("longName",symbol)
    file_name = clean_name(file_name)+"_"+ticker_interval

    data_history = ticker.history(start="2000-01-01", end="2025-07-23", interval=ticker_interval)

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

# ------------------------
# Opción 1: input.txt
# ------------------------
def get_symbol_from_txt(path="input.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            symbol = f.readline().strip().upper()
            if not symbol:
                raise ValueError("El archivo está vacío.")
            return symbol
    except FileNotFoundError:
        print("❌ Archivo input.txt no encontrado.")
        return None    

# 🧪 Ejemplo de uso
if __name__ == "__main__":

    symbol = get_symbol_from_txt()
    interval = ["1mo","1d"]

    if symbol:
        for i in interval:
            save_historical_ticker(symbol,i)  # Cambia por cualquier símbolo: MSFT, SPY, BTC-USD, etc.
            sleep(2)