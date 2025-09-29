from pathlib import Path
import src.UP.Riesgos.utils.utils as utils
import pandas as pd
import numpy as np
import scipy.stats as stats

FILE_NAME="curva_usd_3"
SEED = 42
np.random.seed(SEED)


OUTPUT_DIR = Path(__file__).resolve().parent / "output"
INPUT_DIR = Path(__file__).resolve().parent / "data"

def main():
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

    df_monthly_mean = df.resample("ME").mean()
    df_monthly_mean["diff"] = df_monthly_mean["Rate"].pct_change()
    df_monthly_mean = df_monthly_mean.dropna(subset=["diff"])
    mean_diff_mean, std_diff_mean = df_monthly_mean["diff"].mean(), df_monthly_mean["diff"].std()

    # data = tu serie de datos en un array o columna de DataFrame
    df_input = df_monthly_begin.copy()
    col = "Rate"
    dfr, loc, scale = stats.t.fit(df_input[col])

    print(f"Grados de libertad (df): {dfr:.2f}")
    print(f"Media: {loc:.4f}")
    print(f"Escala: {scale:.4f}")


    if FILE_NAME == "curva_pen_1" or FILE_NAME == "curva_pen_3":
        print("Shock con distribucion normal")
        df_monthly_future = utils.generar_futures_cupon(df_input, mean_diff_begin, std_diff_begin,
                                                    loc, scale, dfr, "2025-08-01", "2031-12-31", "Date", "Rate", "diff", "normal","MS")
    elif FILE_NAME == "curva_usd_1" or FILE_NAME == "curva_usd_3":
        print("Shock con distribucion t-Student")
        df_monthly_future = utils.generar_futures_cupon(df_input, mean_diff_begin, std_diff_begin,
                                                    loc, scale, dfr, "2025-08-01", "2031-12-31", "Date", "Rate", "diff", "t-Student","MS")

    df_extended = pd.concat([df_monthly_begin, df_monthly_future])

    utils.genera_csv(df_extended, f"{OUTPUT_DIR}/{FILE_NAME}_completo")

    return 

if __name__ == "__main__":
    main()
