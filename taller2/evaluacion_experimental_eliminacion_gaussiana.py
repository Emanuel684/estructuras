import json
import random
import time

import matplotlib.pyplot as plt
import numpy as np
from matriz import Matriz


def generar_matriz_aleatoria(n):
    """Genera una matriz aleatoria de tamaño n x (n+1)."""
    matriz = Matriz(n, n + 1)
    for i in range(n):
        for j in range(n + 1):
            matriz.asignar(i, j, random.uniform(-10, 10))
    return matriz


def evaluar_tiempo_promedio(n, repeticiones=10):
    """Evalúa el tiempo promedio para una matriz de tamaño n."""
    tiempos = []
    for _ in range(repeticiones):
        matriz = generar_matriz_aleatoria(n)
        inicio = time.time()
        matriz.eliminacion_gaussiana()
        fin = time.time()
        tiempos.append(fin - inicio)
    return sum(tiempos) / repeticiones


# Rango de valores de N
valores_n = range(10, 101, 10)
tiempos_promedio = [evaluar_tiempo_promedio(n) for n in valores_n]

# Tabular los datos
print("N\tTiempo Promedio (s)")
datos = {}
for n, tiempo in zip(valores_n, tiempos_promedio):
    print(f"{n}\t{tiempo:.6f}")
    datos[f"{n}"] = tiempo

with open("datos_tiempos.json", "w") as fp:
    json.dump(datos, fp)

# Datos experimentales
x = np.array(valores_n)
y = np.array(tiempos_promedio)

# Ajustar una curva cúbica
coeficientes = np.polyfit(x, y, 3)
polinomio = np.poly1d(coeficientes)

# Graficar
plt.scatter(x, y, label="Datos Experimentales")
plt.plot(x, polinomio(x), label=f"Ajuste: {polinomio}", color="red")
plt.xlabel("Tamaño de la matriz (N)")
plt.ylabel("Tiempo Promedio (s)")
plt.legend()
plt.show()
