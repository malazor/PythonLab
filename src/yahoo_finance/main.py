from src.yahoo_finance.utils.tickers.ticker import Ticker
from src.yahoo_finance.constants import DATE_INTERVAL, MONTH_INTERVAL, WEEK_INTERVAL, DATE5_INTERVAL
import numpy as np
from src.yahoo_finance.utils.tickers.calculations import UtilsCalculations 

tickt = Ticker("META")

data_history = tickt.get_filtered_data('2025-01-01','2025-07-31',DATE_INTERVAL)

minimo = data_history["Low"].min()
ultimo_precio = data_history["Close"].iloc[-1]

print(f"Mínimo periodo: {minimo}")
print(f"Ultimo pprecio: {ultimo_precio}")
