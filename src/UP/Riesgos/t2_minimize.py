import numpy as np
from scipy.optimize import root_scalar

def VAN(flujos, r):
    """
    flujos: array de flujos, primer elemento = préstamo inicial (negativo)
    r: tasa por periodo (decimal)
    """
    n_periodos = len(flujos)
    return np.sum(flujos / (1 + r)**np.arange(n_periodos))

def TIR(flujos):
    """
    Devuelve la TIR aproximada por periodo
    """
    # buscamos r tal que VAN(flujos, r) = 0
    result = root_scalar(lambda r: VAN(flujos, r), bracket=[-0.99, 1], method='bisect')
    return result.root if result.converged else None



tc_ini = np.array([
    3.534683303,
    3.534683303,
    3.534683303,
    3.534683303,
    3.581000308,
    3.581000308,
    3.581000308,
    3.581000308,
    3.529122195,
    3.529122195,
    3.529122195,
    3.529122195
])
tasas = np.array([
    0.017583617,
    0.020347561,
    0.019704639,
    0.020988958,
    0.018132806,
    0.019316889,
    0.020023725,
    0.023475733,
    0.017516581,
    0.02221943,
    0.021141735,
    0.023010876
])

matriz_tc = np.array([
    [3.488554519, 3.447923048, 0, 0, 0, 0],
    [3.488554519, 3.447923048, 0, 0, 0, 0],
    [3.488554519, 3.447923048, 3.462958466, 3.362322333, 3.578762371, 3.441138942],
    [3.488554519, 3.447923048, 3.462958466, 3.362322333, 3.578762371, 3.441138942],
    [3.462958466, 3.362322333, 0, 0, 0, 0],
    [3.462958466, 3.362322333, 0, 0, 0, 0],
    [3.462958466, 3.362322333, 3.578762371, 3.441138942, 3.494066212, 3.379628637],
    [3.462958466, 3.362322333, 3.578762371, 3.441138942, 3.494066212, 3.379628637],
    [3.578762371, 3.441138942, 0, 0, 0, 0],
    [3.578762371, 3.441138942, 0, 0, 0, 0],
    [3.578762371, 3.441138942, 3.494066212, 3.379628637, 3.427956997, 3.560693401],
    [3.578762371, 3.441138942, 3.494066212, 3.379628637, 3.427956997, 3.560693401]
])

# matriz_tc original de 12x6 (ya definida)
matriz_4filas = matriz_tc[:4, :]  # filas 0 a 3

# Vector de incógnicas (12 variables)
w = np.array([0.0]*12)  # valores iniciales, se actualizarán en optimización
w[0]=14850000 
w[1]=50000 
w[2]=50000 
w[3]=50000 
w[4]=7500000 
w[5]=7500000
w[6]=7500000
w[7]=7500000
w[8]=6500000
w[9]=9000000
w[10]=1500000
w[11]=3000000

tir = np.array([0.0]*12)
van = np.array([0.0]*12)

# Restricciones de suma por bloque
restricciones = [
    {'type': 'eq', 'fun': lambda w: np.sum(w[0:4]) - 15000000},  # bloque 1: w1+w2+w3+w4 = 15M
    {'type': 'eq', 'fun': lambda w: np.sum(w[4:8]) - 30000000},  # bloque 2: w5+w6+w7+w8 = 30M
    {'type': 'eq', 'fun': lambda w: np.sum(w[8:12]) - 20000000}  # bloque 3: w9+w10+w11+w12 = 20M
]

# También podemos definir límites por variable si quieres
# Ejemplo: cada w >= 0
limites = [(0, None)] * 12

x= 12
y= 7
flujos = np.zeros((x, y))

for i in range(12):
  prestamo_inicial=0
  cuota1=0
  cuota2=0
  cuota3=0
  cuota4=0
  cuota5=0
  cuota6=0  
  if i ==0 or i==4 or i==8:
    prestamo_inicial = - w[i] * tc_ini[i]
    cuota1 = -prestamo_inicial * tasas[i]
    cuota2 = -prestamo_inicial * (1 + tasas[i])
    cuota3 = 0
    cuota4 = 0
    cuota5 = 0
    cuota6 = 0
  elif i==1 or i==5 or i==9:
    prestamo_inicial = - w[i] * tc_ini[i]
    cuota1 = w[i] * tasas[i]* matriz_tc[i,0]
    cuota2 = w[i] * (1*tc_ini[i]+ tasas[i]*matriz_tc[i,1])
    cuota3 = 0
    cuota4 = 0
    cuota5 = 0
    cuota6 = 0
  elif i==2 or i==6 or i==10:
    prestamo_inicial = - w[i] * tc_ini[i]
    cuota1 = -prestamo_inicial * tasas[i]
    cuota2 = -prestamo_inicial * tasas[i]
    cuota3 = -prestamo_inicial * tasas[i]
    cuota4 = -prestamo_inicial * tasas[i]
    cuota5 = -prestamo_inicial * tasas[i]
    cuota6 = -prestamo_inicial * (1 + tasas[i])
  elif i==3 or i==7 or i==11:
    prestamo_inicial = - w[i] * tc_ini[i]
    cuota1 = w[i] * tasas[i]* matriz_tc[i,0]
    cuota2 = w[i] * tasas[i]* matriz_tc[i,1]
    cuota3 = w[i] * tasas[i]* matriz_tc[i,2]
    cuota4 = w[i] * tasas[i]* matriz_tc[i,3]
    cuota5 = w[i] * tasas[i]* matriz_tc[i,4]
    cuota6 = w[i] * (1*tc_ini[i]+ tasas[i]*matriz_tc[i,5])

  # Calculo VAN
  cuotas=[]
  cuotas.append(prestamo_inicial)
  cuotas.append(cuota1)
  cuotas.append(cuota2)
  cuotas.append(cuota3)
  cuotas.append(cuota4)
  cuotas.append(cuota5)
  cuotas.append(cuota6)
  van[i]=VAN(cuotas,tasas[i])
  tir[i]=TIR(cuotas)

  flujos[i,0] = prestamo_inicial
  flujos[i,1] = cuota1
  flujos[i,2] = cuota2
  flujos[i,3] = cuota3
  flujos[i,4] = cuota4
  flujos[i,5] = cuota5
  flujos[i,6] = cuota6
print(flujos)
print("-"*30)

for i in range(len(tir)):
    print(tir[i])


