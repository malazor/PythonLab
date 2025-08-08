import os
import pandas as pd
import numpy as np
from datetime import datetime
import argparse
import yfinance as yf
import re


from src.yahoo_finance.utils.utils import clean_name


def read_csv(symbol, start_date, end_date, ticker_interval):
    RF=0.044

    try:
        # Validar intervalo
        if (ticker_interval=="1mo"):
            yearly_factor=12
        elif (ticker_interval=="1d"):
            yearly_factor=252
        else:
            raise ValueError("Parámetro inválido: debe ser 1mo o 1d")

        # Mapear el nombre del arhivo
        ticker = yf.Ticker(symbol)

        info = ticker.info

        file_name = info.get("longName",symbol)
        file_name = clean_name(file_name)+"_"+ticker_interval

        # Ruta del directorio actual (este script)
        dir_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta del directorio padre (donde está "data")
        parent_dir = os.path.dirname(dir_script)

        # Construye la ruta completa al archivo CSV
        ruta_csv = os.path.join(parent_dir, "data", file_name+".csv")

        # Intenta leer el archivo
        df = pd.read_csv(ruta_csv)

        df["Date"] = pd.to_datetime(df["Date"], utc=True, errors="coerce")


        if start_date and end_date:
            dt_start_date = pd.to_datetime(start_date, utc=True)
            dt_end_date = pd.to_datetime(end_date, utc=True)
            df_filtrado = df[(df["Date"] >= dt_start_date) & (df["Date"] <= dt_end_date)]
        elif start_date:
            dt_start_date = pd.to_datetime(start_date, utc=True)
            df_filtrado = df[(df["Date"] >= dt_start_date)]
        elif end_date:
            dt_end_date = pd.to_datetime(end_date, utc=True)
            df_filtrado = df[(df["Date"] <= dt_end_date)]

        # Calcular retornos
        prices = df_filtrado[["Date","Close"]].copy()
        returns = pd.DataFrame()
        returns["Date"] = prices["Date"]
        returns["Close"] = np.log(prices["Close"]/prices["Close"].shift(1))
        returns= returns.dropna()


        # Warning datos desactualizados
        # Obtener fecha de creación del archivo

        # Fecha de creacion
        # timestamp_creacion = os.path.getctime(ruta_csv)

        # Fecha de creacion
        timestamp_creacion = os.path.getmtime(ruta_csv)

        fecha_creacion = datetime.fromtimestamp(timestamp_creacion).date()
        fecha_hoy = datetime.today().date()

        # Validar si el archivo es del día
        if fecha_creacion < fecha_hoy:
            print("\n⚠️⚠️⚠️  ADVERTENCIA IMPORTANTE  ⚠️⚠️⚠️")
            print(f"🗂️ Fecha de creación del archivo: {fecha_creacion}")
            print(f"📅 Fecha actual: {fecha_hoy}")
            print(f"📅 Archivo: {ruta_csv}")
            print("🟥 El archivo no está actualizado. Se recomienda ejecutar el módulo de descarga.\n")
        else:
            print("📁 Archivo actualizado al día de hoy.")


        print(f"✅ Archivo cargado correctamente: {file_name}")

        print("\n" + "="*60)
        print("🧾 RESUMEN DE PARÁMETROS DE ENTRADA")
        print("="*60)
        print(f"📈 Activo        : {info.get("longName",symbol)}")
        print(f"⏱️ Intervalo     : {ticker_interval}")
        print(f"📅 Fecha inicio  : {start_date}")
        print(f"📅 Fecha fin     : {end_date}")
        print("="*60 + "\n")

        month_mean = returns["Close"].mean()
        month_std_dev = returns["Close"].std()
        anual_mean = yearly_factor*(returns["Close"].mean())
        anual_std_dev = returns["Close"].std()*np.sqrt(yearly_factor)
        sharpe_rate = (anual_mean-RF)/anual_std_dev

        print(f"Media retorno mensual: {100*month_mean:.4f}%")
        print(f"Volatilidad mensual: {100*month_std_dev:.4f}%")
        print(f"Media retorno anual: {100*anual_mean:.4f}%")
        print(f"Volatilidad anual: {100*anual_std_dev:.4f}%")

        print(f"\nRatio Sharpe: {sharpe_rate:.4f}\n")

        return returns

    except FileNotFoundError:
        print(f"❌ El archivo '{file_name}' no se encontró en la carpeta 'data/'.")
        return None
    except pd.errors.ParserError:
        print(f"❌ Error al parsear el archivo CSV: {file_name}")
        return None
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        return None

# 🧪 Ejemplo de uso
if __name__ == "__main__":
    # Fecha actual
    today = datetime.today().date()
    one_year_before = today.replace(year=today.year - 1)

    # Configurar parametros    
    parser = argparse.ArgumentParser(description="Lee y filtra un archivo CSV de datos financieros.")
    parser.add_argument("--symbol", required=True, type=str, help="Símbolo del activo (ej. AAPL)")
    parser.add_argument("--start", type=str, default=str(one_year_before), help="Fecha de inicio (YYYY-MM-DD)")
    parser.add_argument("--end", type=str, default=str(today), help="Fecha de fin (YYYY-MM-DD)")
    parser.add_argument("--interval", type=str, default=str("1mo"), help="Puede ser 1mo o 1d")
    args = parser.parse_args()

    # Cambia esto por el nombre del archivo generado (respetando extensión y nombre limpio)
    read_csv(args.symbol, args.start, args.end, args.interval)
