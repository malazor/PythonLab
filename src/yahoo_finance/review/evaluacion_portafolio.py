import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ----- Configuración -----
activos = ["SPY", "IDEV", "EMXC", "MCHI", "GOVT", "GLD"]

inicio = "2022-01-01"
rf_anual = 0.045  # Tasa libre de riesgo en proporción

# ----- Descargar precios -----
data = yf.download(activos, start=inicio)['Close']
retornos = np.log(data / data.shift(1)).dropna()

# ----- Estadísticas anuales -----
media_anual = retornos.mean() * 252
cov_anual = retornos.cov() * 252

# ----- Simulación de portafolios -----
n_portafolios = 100_000
pesos_lista = []
sharpe_lista = []
retornos_lista = []
volatilidades_lista = []

np.random.seed(42)

for _ in range(n_portafolios):
    pesos = np.random.random(len(activos))
    pesos /= pesos.sum()  # Normalizar
    rendimiento = np.dot(pesos, media_anual)
    volatilidad = np.sqrt(np.dot(pesos.T, np.dot(cov_anual, pesos)))
    sharpe = (rendimiento - rf_anual) / volatilidad

    pesos_lista.append(pesos)
    retornos_lista.append(rendimiento)
    volatilidades_lista.append(volatilidad)
    sharpe_lista.append(sharpe)

# ----- Encontrar portafolio óptimo -----
max_sharpe_idx = np.argmax(sharpe_lista)
mejores_pesos = pesos_lista[max_sharpe_idx]

# ----- Mostrar resultados -----
print("\n📌 Portafolio con mayor Sharpe Ratio:\n")
for activo, peso in zip(activos, mejores_pesos):
    print(f"{activo:5}: {peso:.2%}")

print(f"\n📈 Rendimiento esperado: {retornos_lista[max_sharpe_idx]:.2%}")
print(f"📉 Volatilidad esperada: {volatilidades_lista[max_sharpe_idx]:.2%}")
print(f"🧮 Sharpe Ratio: {sharpe_lista[max_sharpe_idx]:.4f}")

# ----- Graficar portafolios -----
plt.figure(figsize=(10, 6))
plt.scatter(volatilidades_lista, retornos_lista, c=sharpe_lista, cmap='viridis', alpha=0.5)
plt.colorbar(label='Sharpe Ratio')
plt.scatter(volatilidades_lista[max_sharpe_idx], retornos_lista[max_sharpe_idx], color='red', s=100, label='Máximo Sharpe')
plt.xlabel("Volatilidad")
plt.ylabel("Retorno Esperado")
plt.title("Portafolios simulados y Ratio Sharpe")
plt.legend()
plt.grid(True)
plt.show()
