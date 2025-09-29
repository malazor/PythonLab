from pathlib import Path
import src.UP.Riesgos.utils.utils as utils
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

FILE_NAME="curva_usd_3"

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
INPUT_DIR = Path(__file__).resolve().parent / "data"

def main():
    # Descargar histórico diario de USDPEN desde Yahoo Finance
    ticker = "USDPEN=X"
    start_date = "2022-12-31"
    end_date = "2025-08-31"
    interval = "1d"

    # df = utils.yfinance_download(ticker, start_date, end_date, interval)
    # utils.genera_csv(df, f"{OUTPUT_DIR}/TC_USDPEN")

    df = utils.leer_csv(f"{INPUT_DIR}/{FILE_NAME}.csv", sep=";")

    df["Rate"] = df["Rate"].astype(float)
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
    df = df.set_index("Date")

    print(FILE_NAME)
    print(f"Media: {df['Rate'].mean()}")
    print(f"Desviacion Std: {df['Rate'].std()}")

    # Reamostrar a fin de mes (último día hábil de cada mes)
    df_monthly_last = df.resample("ME").last()
    df_monthly_last["diff"] = df_monthly_last["Rate"].pct_change()
    df_monthly_last = df_monthly_last.dropna(subset=["diff"])
    mean_diff_last, std_diff_last = df_monthly_last["diff"].mean(), df_monthly_last["diff"].std()

    df_monthly_begin = df.resample("MS").first()
    df_monthly_begin["diff"] = df_monthly_begin["Rate"].pct_change()
    df_monthly_begin = df_monthly_begin.dropna(subset=["diff"])
    mean_diff_begin, std_diff_begin = df_monthly_begin["diff"].mean(), df_monthly_begin["diff"].std()

    # df = df["Close"]

    # output = utils.analizar_distribucion(df_monthly_last,FILE_NAME, "diff")
    # print(output)

    return 

if __name__ == "__main__":
    main()
