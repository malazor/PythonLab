import pandas as pd
from datetime import datetime
import os
import json
from src.yahoo_finance.constants import DATA_DIR, SYMBOL_DICT_FILE, DATE_INTERVAL, MONTH_INTERVAL, DATE5_INTERVAL, WEEK_INTERVAL, YF_DATE, YF_CLOSE, FACTOR_DTM, FACTOR_DTW, FACTOR_DTY, FACTOR_MTY
from src.yahoo_finance.utils.utils import clean_name, load_json
import yfinance as yf
import numpy as np


class Ticker:
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        self.clean_name = clean_name(symbol)
        self.cfg_file = self.get_cfg_file_name()
        self.info = self.load_info()

        self.history_data_1d = None
        self.history_data_5d = None
        self.history_data_1wk = None
        self.history_data_1mo = None

        self.returns = None

        self.dividends = None
        self.splits = None
        self.fetched_at = None

    def get_cfg_file_name(self):
        # Ruta del directorio que contiene el script
        dir_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta al directorio padre (uno arriba)
        parent_dir = os.path.dirname(os.path.dirname(dir_script))

        # Se construye la ruta para que este dentro de la carpeta data
        # Ruta de la carpeta "data" al mismo nivel que el script
        data_file = os.path.join(parent_dir, DATA_DIR,SYMBOL_DICT_FILE)

        with open(data_file, 'r') as f:
            cfg_symbol=json.load(f)
            return cfg_symbol[self.symbol]
    
    def load_info(self):
        # Ruta del directorio que contiene el script
        dir_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta al directorio padre (uno arriba)
        parent_dir = os.path.dirname(os.path.dirname(dir_script))

        # Se construye la ruta para que este dentro de la carpeta data
        # Ruta de la carpeta "data" al mismo nivel que el script
        data_file = os.path.join(parent_dir, DATA_DIR,f"{self.cfg_file}.json")

        with open(data_file, 'r') as f:
            ticker_info=json.load(f)

        return ticker_info

    def load_history(self,interval):
        # Ruta del directorio que contiene el script
        dir_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta al directorio padre (uno arriba)
        parent_dir = os.path.dirname(os.path.dirname(dir_script))

        # Se construye la ruta para que este dentro de la carpeta data
        # Ruta de la carpeta "data" al mismo nivel que el script
        data_file = os.path.join(parent_dir, DATA_DIR,f"{clean_name(self.info["longName"])}_{interval}.csv")

        if interval==DATE_INTERVAL:
            self.history_data_1d = pd.read_csv(data_file, sep=",")
        elif interval==MONTH_INTERVAL:
            self.history_data_1mo = pd.read_csv(data_file, sep=",")
        elif interval==WEEK_INTERVAL:
            self.history_data_1wk = pd.read_csv(data_file, sep=",")
        elif interval==DATE5_INTERVAL:
            self.history_data_1d5 = pd.read_csv(data_file, sep=",")
    
    def get_last_update(self):
        tck = yf.Ticker(self.symbol)
        df = tck.history(period=DATE_INTERVAL, interval="1m")

        # Mostrar el último valor
        ultimo_registro = df.tail(1)
        return ultimo_registro

    def get_filtered_data(self, start_date, end_date, interval):

        try:
            output = {}
            dt_start_date=pd.to_datetime(start_date, utc=True)
            dt_end_date=pd.to_datetime(end_date, utc=True)

            if (interval == DATE_INTERVAL):
                self.load_history(DATE_INTERVAL)
                df = self.history_data_1d
            elif (interval == MONTH_INTERVAL):
                self.load_history(MONTH_INTERVAL)
                df = self.history_data_1mo
            elif (interval == WEEK_INTERVAL):
                self.load_history(WEEK_INTERVAL)
                df = self.history_data_1wk
            elif (interval == DATE5_INTERVAL):
                self.load_history(DATE5_INTERVAL)
                df = self.history_data_1d5

            df[YF_DATE] = pd.to_datetime(df[YF_DATE], errors="raise", utc=True)

            data_filtered = df[(df[YF_DATE]>= dt_start_date) & (df[YF_DATE]<= dt_end_date)]
            close_returns = self.calculate_diff_log(data_filtered)
            output["data"]= data_filtered
            output["returns_close"] = close_returns

            output["return_mean"] = float(close_returns[YF_CLOSE].mean())
            output["return_max"] = float(close_returns[YF_CLOSE].max())
            output["return_min"] = float(close_returns[YF_CLOSE].min())
            output["return_var"] = float(close_returns[YF_CLOSE].var())
            output["return_std"] = float(close_returns[YF_CLOSE].std())
            output["return_count"] = float(close_returns[YF_CLOSE].count())

            if (interval == DATE_INTERVAL):

                output["yearly_volatility"] = output["return_mean"]*FACTOR_DTY
                output["monthly_volatility"] = output["return_mean"]*FACTOR_DTM
                output["weekly_volatility"] = output["return_mean"]*FACTOR_DTW                
            elif (interval == MONTH_INTERVAL):
                output["yearly_volatility"] = output["return_mean"]*FACTOR_MTY
                output["monthly_volatility"] = output["return_mean"]*FACTOR_DTM
                output["weekly_volatility"] = output["return_mean"]*FACTOR_DTW                
            elif (interval == WEEK_INTERVAL):
                self.load_history(WEEK_INTERVAL)
                df = self.history_data_1wk
            elif (interval == DATE5_INTERVAL):
                self.load_history(DATE5_INTERVAL)
                df = self.history_data_1d5


            return output

        except TypeError as e:
            print("Error de tipo de dato incorrecto:")
            print(e)
        except Exception as e:
            print("Error general:")
            print(type(e))

    def calculate_diff_log(self,input_series):
        df = input_series.copy()
        df[YF_DATE] = pd.to_datetime(df[YF_DATE])
        df = df.sort_values(YF_DATE)

        # Calcular log-return
        df[YF_CLOSE] = np.log(df[YF_CLOSE] / df[YF_CLOSE].shift(1))

        # Eliminar el primer valor NaN (por el shift)
        df = df.dropna(subset=[YF_CLOSE])

        # Devolver solo las columnas Date y Diff
        return df[[YF_DATE, YF_CLOSE]]
    
    def calculate_diff_simple(input_series):
        output  = output.pct_change()
        output = output.dropna()
        return output

    def fetch_info(self):
        """Carga la información general del ticker"""
        self.info = self._ticker.info
        self.fetched_at = datetime.now()

    def fetch_history(self, period='1y', interval='1d'):
        """Obtiene precios históricos"""
        self.history_data = self._ticker.history(period=period, interval=interval)
        self.fetched_at = datetime.now()

    def fetch_actions(self):
        """Acciones corporativas (dividendos y splits)"""
        self.actions = self._ticker.actions
        self.dividends = self._ticker.dividends
        self.splits = self._ticker.splits

    def show_summary(self):
        """Imprime resumen rápido de la empresa"""
        if self.info is None:
            self.fetch_info()

        print(f"--- {self.symbol} ---")
        print(f"Nombre: {self.info.get('longName')}")
        print(f"Sector: {self.info.get('sector')}")
        print(f"Industria: {self.info.get('industry')}")
        print(f"Precio actual: {self.info.get('currentPrice')}")
        print(f"Capitalización: {self.info.get('marketCap')}")
        print(f"País: {self.info.get('country')}")
        print(f"Última actualización: {self.fetched_at.strftime('%Y-%m-%d %H:%M:%S')}" if self.fetched_at else "No actualizado")

    def get_return(self, method='log'):
        """Calcula el retorno del precio de cierre ajustado"""
        if self.history_data is None:
            self.fetch_history()
        prices = self.history_data['Close']
        if method == 'log':
            return (prices / prices.shift(1)).apply(lambda x: pd.np.log(x))
        else:
            return prices.pct_change()
