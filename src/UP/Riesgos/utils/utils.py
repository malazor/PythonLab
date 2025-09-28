import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import pandas as pd

from pathlib import Path

def leer_csv(path: Path) -> pd.DataFrame:
    # sep=None permite inferir coma/; | utf-8-sig cubre BOM
    return pd.read_csv(path, sep=None, engine="python", encoding="utf-8-sig", on_bad_lines="skip")

def genera_csv(df, name):
    # Guardar en CSV
    output_file = name + ".csv"
    df.to_csv(output_file, index=True, date_format="%Y-%m-%d")


def generar_shock_normal(media, desvest, seed):
    rng = np.random.default_rng(seed)
    return rng.normal(loc=media, scale=desvest)

def generar_shock_t(media, desvest, seed):
    rng = np.random.default_rng(seed)
#    return rng.normal(loc=media, scale=desvest)
    return rng.standard_t(loc=media, scale=desvest)


def analizar_distribucion(df: pd.DataFrame, col: str = "Close"):
    """
    Analiza la distribución de una serie en un DataFrame:
    
    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame que contiene la serie temporal.
    col : str
        Nombre de la columna a analizar (por defecto "Close").
    
    Salidas:
    --------
    - Gráficos: Histograma + curvas Normal y t-Student
    - Q-Q plots contra Normal y t-Student
    - Resultados estadísticos (Shapiro-Wilk y KS Tests)
    """

#     data = df[col].dropna()
    data = df[col].astype(float).dropna().values


    # === 1. Ajuste de Normal y t-Student ===
    mu, sigma = stats.norm.fit(data)                     # Normal
    df_t, loc_t, scale_t = stats.t.fit(data)             # t-Student

    # Rango para curvas
#    x = np.linspace(min(data), max(data), 500)
    x = np.linspace(data.min(), data.max(), 500)


    # === 2. Gráfico: histograma + curvas ===
    plt.figure(figsize=(10,5))
    plt.hist(data, bins=30, density=True, alpha=0.6, color="skyblue", edgecolor="black", label="Datos")
    plt.plot(x, stats.norm.pdf(x, mu, sigma), "r-", lw=2, label=f"Normal (μ={mu:.2f}, σ={sigma:.2f})")
    plt.plot(x, stats.t.pdf(x, df_t, loc_t, scale_t), "g--", lw=2, label=f"t-Student (df={df_t:.1f})")
    plt.title(f"Exploración de distribución ({col})")
    plt.xlabel(col)
    plt.ylabel("Densidad")
    plt.legend()
    plt.show()

    # === 3. Q-Q plots ===
    sm.qqplot(data, line="s", dist=stats.norm, fit=True)
    plt.title("Q-Q plot contra Normal")
    plt.show()

    sm.qqplot(data, line="s", dist=stats.t, distargs=(df_t,), fit=True)
    plt.title("Q-Q plot contra t-Student")
    plt.show()

    # === 4. Pruebas estadísticas ===
    # Shapiro-Wilk (normalidad)
    stat_shapiro, p_shapiro = stats.shapiro(data)

    # Kolmogorov-Smirnov contra Normal
    stat_ks_norm, p_ks_norm = stats.kstest(data, "norm", args=(mu, sigma))

    # Kolmogorov-Smirnov contra t-Student
    stat_ks_t, p_ks_t = stats.kstest(data, "t", args=(df_t, loc_t, scale_t))

    # Resultados
    resultados = {
        "Shapiro-Wilk": {"stat": stat_shapiro, "pvalue": p_shapiro},
        "KS Normal": {"stat": stat_ks_norm, "pvalue": p_ks_norm},
        "KS t-Student": {"stat": stat_ks_t, "pvalue": p_ks_t}
    }

    print("=== Resultados estadísticos ===")
    for test, res in resultados.items():
        stat = float(res['stat'])
        pval = float(res['pvalue'])
        print(f"{test}: stat={stat:.3f}, p={pval:.3f}")        

    print("\nInterpretación rápida:")
    print("- p > 0.05 → no se rechaza la hipótesis nula (la distribución puede encajar).")
    print("- p < 0.05 → se rechaza la hipótesis nula (la distribución no encaja).")

    return resultados


def simulacion_tc(df_future, mean_diff, std_diff, SEED):
    # Primer día 2026
    # val_2026_1 = df_future.loc["2026-01-01", "Close"]

    # Último día semestre de 2026
    val_2026_2 = df_future.loc["2026-06-30", "Close"]

    # Último día de 2026
    val_2026_3 = df_future.loc["2026-12-31", "Close"]

    # Primer día 2027
    # val_2027_1 = df_future.loc["2027-01-01", "Close"]

    # Último día semestre de 2027
    val_2027_2 = df_future.loc["2027-06-30", "Close"]

    # Último día de 2027
    val_2027_3 = df_future.loc["2027-12-31", "Close"]

    # Primer día 2028
    # val_2028_1 = df_future.loc["2028-01-01", "Close"]

    # Último día semestre de 2028
    val_2028_2 = df_future.loc["2028-06-30", "Close"]

    # Último día de 2028
    val_2028_3 = df_future.loc["2028-12-31", "Close"]

    # Primer día 2029
    # val_2029_1 = df_future.loc["2029-01-01", "Close"]

   # Último día semestre de 2029
    val_2029_2 = df_future.loc["2029-06-30", "Close"]

    # Último día de 2029
    val_2029_3 = df_future.loc["2029-12-31", "Close"]

    # Primer día 2030
    # val_2030_1 = df_future.loc["2030-01-01", "Close"]

    # Último día semestre de 2030
    val_2030_2 = df_future.loc["2030-06-30", "Close"]

    # Último día de 2030
    val_2030_3 = df_future.loc["2030-12-31", "Close"]

    # Simulación encadenada
    base_values = [val_2026_2, val_2026_3, val_2027_2, val_2027_3, val_2028_2, val_2028_3, val_2029_2, val_2029_3, val_2030_2, val_2030_3]
    years = ["2026-1", "2026-2", "2027-1", "2027-2", "2028-1", "2028-2", "2029-1", "2029-2", "2030-1", "2030-2"]

    n_iter = 10000
    results = []

    for i in range(n_iter):
        if i == 0:
            # Iteración 0: valores base
            results.append(base_values)
        else:
            shocked_values = []
            shock=generar_shock_normal(mean_diff, std_diff,SEED)
            prev_value = base_values[0] * (1 + shock/100)
            shocked_values.append(prev_value)
            for j in range(1, len(base_values)):
                t_shock = generar_shock_normal(mean_diff, std_diff,SEED)
                prev_value = prev_value * (1 + t_shock/100)
                print(f"Prev value: {prev_value} - Shock: {shock}")
                shocked_values.append(prev_value)
            results.append(shocked_values)

    # Crear DataFrame
    df_sim = pd.DataFrame(results, columns=years)

    return df_sim

#   print(df_sim.median().to_frame(name="Mediana"))

def simulacion_cupon(df_future, mean_diff, std_diff, SEED):
    # Último día semestre de 2026
    val_2026_1 = df_future.loc["2026-01-31", "Close"]

    # Último día semestre de 2027
    val_2027_1 = df_future.loc["2027-01-31", "Close"]

    # Último día semestre de 2028
    val_2028_1 = df_future.loc["2028-01-31", "Close"]

    # Simulación encadenada
    base_values = [val_2026_1, val_2027_1, val_2028_1]
    years = ["2026-1", "2027-1", "2028-1"]

    n_iter = 10000
    results = []

    for i in range(n_iter):
        if i == 0:
            # Iteración 0: valores base
            results.append(base_values)
        else:
            shocked_values = []
            prev_value = base_values[0] * (1 + generar_shock_normal(mean_diff, std_diff,SEED)/100)
            shocked_values.append(prev_value)
            for j in range(1, len(base_values)):
                prev_value = prev_value * (1 + generar_shock_normal(mean_diff, std_diff,SEED)/100)
                shocked_values.append(prev_value)
            results.append(shocked_values)

    # Crear DataFrame
    df_sim = pd.DataFrame(results, columns=years)

    return df_sim

#   print(df_sim.median().to_frame(name="Mediana"))