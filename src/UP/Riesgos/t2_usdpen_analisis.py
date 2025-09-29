from pathlib import Path
import src.UP.Riesgos.utils.utils as utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


OUTPUT_DIR = Path(__file__).resolve().parent / "output"

def main():
    # Descargar histórico diario de USDPEN desde Yahoo Finance
    ticker = "USDPEN=X"
    start_date = "2022-12-31"
    end_date = "2025-08-31"
    interval = "1d"

    df = utils.yfinance_download(ticker, start_date, end_date, interval)
    # utils.genera_csv(df, f"{OUTPUT_DIR}/TC_USDPEN")

    #df = utils.leer_csv(f"{OUTPUT_DIR}/TC_USDPEN.csv")

    df["Close"] = df["Close"].astype(float)

    # Reamostrar a fin de mes (último día hábil de cada mes)
    df_monthly_last = df.resample("ME").last()
    df_monthly_last["diff"] = df_monthly_last["Close"].pct_change()
    mean_diff_last, std_diff_last = df_monthly_last["diff"].mean(), df_monthly_last["diff"].std()

    df_monthly_begin = df.resample("MS").first()
    df_monthly_begin["diff"] = df_monthly_begin["Close"].pct_change()
    mean_diff_begin, std_diff_begin = df_monthly_begin["diff"].mean(), df_monthly_begin["diff"].std()


    # df = df["Close"]

    # output = utils.analizar_distribucion(df_monthly_last,"USDPEN", "diff")
    # print(output)

    return 





if __name__ == "__main__":
    main()
