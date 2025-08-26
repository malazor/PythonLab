import pandas as pd
from datetime import datetime
import os
import json
from src.yahoo_finance.utils.utils import clean_name, load_json
import yfinance as yf
import numpy as np
import src.yahoo_finance.constants as cons
from src.yahoo_finance.utils.tickers.calculations import UtilsCalculations


class Ticker:
    def __init__(self, symbol: str):
        self.symbol = symbol.upper()
        self.clean_name = clean_name(symbol)
        self.cfg_file = self.get_cfg_file_name()
        self.info = self.load_info()
        self.name = self.info.get("longName",symbol)
        self.sector = self.info[cons.YF_TICKET_INFO_SECTOR]

        self.data_file = None
        self.history_data_1d = None
        self.history_data_5d = None
        self.history_data_1wk = None
        self.history_data_1mo = None

        self.last_price = self.info[cons.YF_TICKET_INFO_REGULAR_MARKET_PRICE]

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
        data_file = os.path.join(parent_dir, cons.DATA_DIR,cons.SYMBOL_DICT_FILE)

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
        data_file = os.path.join(parent_dir, cons.DATA_DIR,f"{self.cfg_file}.json")

        with open(data_file, 'r') as f:
            ticker_info=json.load(f)

        return ticker_info

    def load_history(self):
        # Ruta del directorio que contiene el script
        dir_script = os.path.dirname(os.path.abspath(__file__))

        # Ruta al directorio padre (uno arriba)
        parent_dir = os.path.dirname(os.path.dirname(dir_script))

        # Se construye la ruta para que este dentro de la carpeta data
        # Ruta de la carpeta "data" al mismo nivel que el script
        data_file_1mo = os.path.join(parent_dir, cons.DATA_DIR,f"{clean_name(self.info["longName"])}_{cons.MONTH_INTERVAL}.csv")
        data_file_1d = os.path.join(parent_dir, cons.DATA_DIR,f"{clean_name(self.info["longName"])}_{cons.DATE_INTERVAL}.csv")
        data_file_1wk = os.path.join(parent_dir, cons.DATA_DIR,f"{clean_name(self.info["longName"])}_{cons.WEEK_INTERVAL}.csv")
        data_file_1d5 = os.path.join(parent_dir, cons.DATA_DIR,f"{clean_name(self.info["longName"])}_{cons.DATE5_INTERVAL}.csv")

        self.data_file = clean_name(self.info["longName"])

        self.history_data_1d = pd.read_csv(data_file_1d, sep=",")
        self.history_data_1mo = pd.read_csv(data_file_1mo, sep=",")
        self.history_data_1wk = pd.read_csv(data_file_1wk, sep=",")
        self.history_data_1d5 = pd.read_csv(data_file_1d5, sep=",")
    
    def get_last_update(self):
        tck = yf.Ticker(self.symbol)
        df = tck.history(period=cons.DATE_INTERVAL, interval=cons.DATE_INTERVAL)

        # Mostrar el último valor
        ultimo_registro = df.tail(1)
        return ultimo_registro[cons.YF_CLOSE].iloc[-1]
    
    def get_filtered_data(self, start_date, end_date, interval):

        try:
            output = {}
            dt_start_date=pd.to_datetime(start_date, utc=True)
            dt_end_date=pd.to_datetime(end_date, utc=True)

            self.load_history()
            if (interval == cons.DATE_INTERVAL):
                df = self.history_data_1d
            elif (interval == cons.MONTH_INTERVAL):
                df = self.history_data_1mo
            elif (interval == cons.WEEK_INTERVAL):
                df = self.history_data_1wk
            elif (interval == cons.DATE5_INTERVAL):
                df = self.history_data_1d5

            df[cons.YF_DATE] = pd.to_datetime(df[cons.YF_DATE], errors="raise", utc=True)

            data_filtered = df[(df[cons.YF_DATE]>= dt_start_date) & (df[cons.YF_DATE]<= dt_end_date)]
            close_returns = self.calculate_diff_log(data_filtered)
            output["data"]= data_filtered
            output["returns_close"] = close_returns

            output["return_mean"] = float(close_returns[cons.YF_CLOSE].mean())
            output["return_max"] = float(close_returns[cons.YF_CLOSE].max())
            output["return_min"] = float(close_returns[cons.YF_CLOSE].min())
            output["return_var"] = float(close_returns[cons.YF_CLOSE].var())
            output["return_std"] = float(close_returns[cons.YF_CLOSE].std())
            output["return_count"] = float(close_returns[cons.YF_CLOSE].count())

            if (interval == cons.DATE_INTERVAL):

                output["yearly_return"] = UtilsCalculations.annualize_return(output["return_mean"])
                output["monthly_return"] = UtilsCalculations.monthly_return_from_daily(output["return_mean"])
                output["weekly_return"] = UtilsCalculations.weekly_return_from_daily(output["return_mean"])

                output["yearly_volatility"] = UtilsCalculations.annualize_volatility(output["return_std"])
                output["monthly_volatility"] = UtilsCalculations.monthly_volatility_from_daily(output["return_std"])
                output["weekly_volatility"] = UtilsCalculations.weekly_volatility_from_daily(output["return_std"])
            elif (interval == cons.MONTH_INTERVAL):
                output["yearly_return"] = UtilsCalculations.annualize_return_from_monthly(output["return_mean"])
                output["monthly_return"] = output["return_mean"]
                output["weekly_return"] = UtilsCalculations.weekly_return_from_monthly(output["return_mean"])

                output["yearly_volatility"] = UtilsCalculations.annualize_volatility_from_monthly(output["return_std"])
                output["monthly_volatility"] = output["return_std"]
                output["weekly_volatility"] = UtilsCalculations.weekly_volatility_from_monthly(output["return_std"])

            return output

        except TypeError as e:
            print("Error de tipo de dato incorrecto:")
            print(e)
        except Exception as e:
            print("Error general:")
            print(type(e))

    def calculate_diff_log(self,input_series):
        df = input_series.copy()
        df[cons.YF_DATE] = pd.to_datetime(df[cons.YF_DATE])
        df = df.sort_values(cons.YF_DATE)

        # Calcular log-return
        df[cons.YF_CLOSE] = np.log(df[cons.YF_CLOSE] / df[cons.YF_CLOSE].shift(1))

        # Eliminar el primer valor NaN (por el shift)
        df = df.dropna(subset=[cons.YF_CLOSE])

        # Devolver solo las columnas Date y Diff
        return df[[cons.YF_DATE, cons.YF_CLOSE]]
    
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

    def get_current_monthly_price(self):
        return self.history_data_1mo[cons.YF_CLOSE].iloc[-1]
    def get_previous_monthly_price(self):
        return self.history_data_1mo[cons.YF_CLOSE].iloc[-2]

    def get_current_daily_price(self):
        return self.history_data_1d[cons.YF_CLOSE].iloc[-1]
    def get_previous_daily_price(self):
        return self.history_data_1d[cons.YF_CLOSE].iloc[-2]
