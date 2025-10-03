import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, brentq

# =========================
# 1. Datos de bonos ficticios
# =========================
bonos = {
    "Bono1": {"precio": 95, "flujos": [5, 105]},             # 2 años
    "Bono2": {"precio": 98, "flujos": [4, 4, 104]},          # 3 años
    "Bono3": {"precio": 90, "flujos": [6, 6, 6, 106]},       # 4 años
    "Bono4": {"precio": 100,"flujos": [3, 3, 3, 3, 103]},    # 5 años
}

# =========================
# 2. Funciones auxiliares
# =========================
def tir_portafolio(weights, bonos):
    precio = sum(w * bonos[b]["precio"] for w, b in zip(weights, bonos))
    max_len = max(len(bonos[b]["flujos"]) for b in bonos)
    flujos = np.zeros(max_len)
    for w, b in zip(weights, bonos):
        fl = np.array(bonos[b]["flujos"])
        flujos[:len(fl)] += w * fl

    def f(r):
        return np.sum(flujos / (1+r)**np.arange(1, len(flujos)+1)) - precio

    try:
        tir = brentq(f, -0.9, 1.0)
    except ValueError:
        tir = np.nan
    return tir

def duracion_portafolio(weights, bonos):
    """Duración de Macaulay"""
    precio = sum(w * bonos[b]["precio"] for w, b in zip(weights, bonos))
    max_len = max(len(bonos[b]["flujos"]) for b in bonos)
    flujos = np.zeros(max_len)
    for w, b in zip(weights, bonos):
        fl = np.array(bonos[b]["flujos"])
        flujos[:len(fl)] += w * fl

    tir = tir_portafolio(weights, bonos)
    if np.isnan(tir):
        return np.nan

    tiempos = np.arange(1, len(flujos)+1)
    vp = flujos / (1+tir)**tiempos
    return np.sum(tiempos * vp) / precio

# =========================
# 3. Simulación de portafolios
# =========================
n_port = 10000
tirs, durs = [], []
for _ in range(n_port):
    w = np.random.random(len(bonos))
    w /= w.sum()
    t = tir_portafolio(w, bonos)
    d = duracion_portafolio(w, bonos)
    if not np.isnan(t) and not np.isnan(d):
        tirs.append(t)
        durs.append(d)

tirs = np.array(tirs)
durs = np.array(durs)

# =========================
# 4. Frontera eficiente (envolvente inferior)
# =========================
sorted_idx = np.argsort(durs)
durs_sorted = durs[sorted_idx]
tirs_sorted = tirs[sorted_idx]

frontera_durs = []
frontera_tirs = []
best_tir = np.inf
for d, t in zip(durs_sorted, tirs_sorted):
    if t < best_tir:
        best_tir = t
        frontera_durs.append(d)
        frontera_tirs.append(t)

# =========================
# 5. Gráficos
# =========================
plt.figure(figsize=(14,6))

# Histograma de TIRs
plt.subplot(1,2,1)
plt.hist(tirs*100, bins=50, alpha=0.6, color="skyblue", edgecolor="k")
plt.axvline(min(tirs)*100, color="red", linestyle="--", label=f"TIR mínima {min(tirs)*100:.2f}%")
plt.title("Distribución de TIRs de portafolios")
plt.xlabel("TIR (%)")
plt.ylabel("Frecuencia")
plt.legend()

# Scatter Duración vs TIR con frontera
plt.subplot(1,2,2)
plt.scatter(durs, tirs*100, alpha=0.4, s=10, label="Portafolios simulados")
plt.plot(frontera_durs, np.array(frontera_tirs)*100, color="red", linewidth=2, label="Frontera eficiente")
plt.xlabel("Duración (años)")
plt.ylabel("TIR (%)")
plt.title("Frontera eficiente de portafolios de deuda")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
