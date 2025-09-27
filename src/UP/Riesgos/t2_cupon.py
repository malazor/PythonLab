# leer_curvas.py
from pathlib import Path
import src.UP.Riesgos.utils.utils as utils
import pandas as pd
import numpy as np

SEED = 42
np.random.seed(SEED)

DATA_DIR = Path(__file__).resolve().parent / "data"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

FILES = {
    "PEN_1Y": "curva_pen_1.csv",
    "PEN_3Y": "curva_pen_3.csv",
    "USD_1Y": "curva_usd_1.csv",
    "USD_3Y": "curva_usd_3.csv",
}

def main():
    dfs = {}
    df_stats = {}
    last_values = {}
    df_future = {}


    for k, fname in FILES.items():

        # Lectura del CSV
        path = DATA_DIR / fname
        df = utils.leer_csv(path)
 
        # Arreglo de tipos de datos
        df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")
        df = df.set_index("Date")

        # Calculo e inclusion del campo Diff diario
        df["Diff"] = df["Rate"].pct_change()*100
        df = df.dropna(subset=["Diff"])

        # Agrupacion por mes
        df_monthly = df.resample("ME").last()
        df_monthly = df_monthly.iloc[:-1] # Se elimina el mes de septiembre pq no esta completo

        # Calculo e inclusion del campo Diff mensual
        df_monthly["Diff"] = df_monthly["Rate"].pct_change() * 100

        # Genera CSV Historico
        utils.genera_csv(df_monthly, f"{OUTPUT_DIR}/{k}_historico")

        # Calculo media y desviacion Diff
        mean_diff, std_diff = df_monthly["Diff"].mean(), df_monthly["Diff"].std()

        # Calcular distribucion de la serie
        # resultados = utils.analizar_distribucion(df_monthly, col="Rate")
        # print(resultados)

        # Guardar datos en diccionario
        df_stats[k] = {"mean":float(mean_diff), "std":float(std_diff)}
        dfs[k] = df_monthly

        # Proyecciones
        future_dates = pd.date_range(start="2025-09-30", end="2031-12-31", freq="ME")

        last_values[k] = float(df_monthly["Rate"].iloc[-1])

        projections = []
        current_value = {}
        current_value[k] = last_values[k]

        for date in future_dates:
            temp = current_value[k]

            shock = utils.generar_shock_normal(mean_diff, std_diff,SEED)
            current_value[k] = current_value[k] * (1 + shock/100)
            last_diff = (current_value[k] - temp)/current_value[k]
            projections.append((date, current_value[k], last_diff))

        df_future[k] = pd.DataFrame(projections, columns=["Fecha", "Close", "diff"]).set_index("Fecha")

        # Genera CSV Futuro
        utils.genera_csv(df_future[k], f"{OUTPUT_DIR}/{k}_futuro")

        # Genera Simulación
        df_sim = utils.simulacion(df_future[k], mean_diff, std_diff, SEED)

        utils.genera_csv(df_sim, f"{OUTPUT_DIR}/{k}_sim")

        print("-"*30)
        print(k)
        print("-"*30)
        print(df_sim.mean().to_frame(name="Media"))        





if __name__ == "__main__":
    main()
