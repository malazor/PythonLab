from pathlib import Path
import src.UP.Riesgos.utils.utils as utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

SEED = 42
np.random.seed(SEED)

FILE_NAME="tc_usdpen"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

def main():
    # Descargar histórico diario de USDPEN desde Yahoo Finance
    ticker = "USDPEN=X"
    start_date = "2022-12-01"
    end_date = "2025-08-31"
    interval = "1d"

    df = utils.yfinance_download(ticker, start_date, end_date, interval)

    df_temp = utils.leer_csv(f"{OUTPUT_DIR}/TC_USDPEN.csv", sep=",", index_col=0)
    df_temp = df_temp.reset_index().rename(columns={"index": "Date"})

    df_end = df_temp[["Date", "Close"]].copy()

    df_end.dropna(inplace=True)

    print(df_end.head(5))
    print(df_end.tail(5))

    df["Close"] = df["Close"].astype(float)

    # Reamostrar a fin de mes (último día hábil de cada mes)
    flag_last="ME"
    df_monthly_last = df.resample(flag_last).last()
    df_monthly_last["diff"] = df_monthly_last["Close"].pct_change()
    mean_diff_last, std_diff_last = df_monthly_last["diff"].mean(), df_monthly_last["diff"].std()

    flag_begin="MS"
    df_monthly_begin = df.resample(flag_begin).first()
    df_monthly_begin["diff"] = df_monthly_begin["Close"].pct_change()
    mean_diff_begin, std_diff_begin = df_monthly_begin["diff"].mean(), df_monthly_begin["diff"].std()

    df_monthly_future_begin = utils.generar_futures_usdpen(df_monthly_begin, mean_diff_begin, std_diff_begin, "2025-09-01", "2031-12-01", "Date", "Close", "diff",seed=SEED, freq=flag_begin)
    df_monthly_future_last = utils.generar_futures_usdpen(df_monthly_last, mean_diff_last, std_diff_last, "2025-09-01", "2031-12-01", "Date", "Close", "diff",seed=SEED, freq=flag_last)

    df_extended_begin = pd.concat([df_monthly_begin["Close"], df_monthly_future_begin["Close"]])
    df_extended_last = pd.concat([df_monthly_last["Close"], df_monthly_future_last["Close"]])

    utils.genera_csv(df_extended_begin, f"{OUTPUT_DIR}/{FILE_NAME}_begin_completo")
    utils.genera_csv(df_extended_last, f"{OUTPUT_DIR}/{FILE_NAME}_last_completo")

    return 





if __name__ == "__main__":
    main()
