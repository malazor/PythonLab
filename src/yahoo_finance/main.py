from src.yahoo_finance.utils.tickers.ticker import Ticker
from src.yahoo_finance.constants import DATE_INTERVAL, MONTH_INTERVAL, WEEK_INTERVAL, DATE5_INTERVAL
import numpy as np

tickt = Ticker("META")

data_history = tickt.get_filtered_data('2025-01-01','2025-07-31',MONTH_INTERVAL)


print(data_history)
# print(tickt.get_filtered_data('2025-01-01','2025-07-31',WEEK_INTERVAL)["data"].describe())
