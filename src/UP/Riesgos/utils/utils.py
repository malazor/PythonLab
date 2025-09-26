import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.api as sm
import pandas as pd


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
