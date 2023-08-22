import numpy as np
import matplotlib.pyplot as plt

#Defino constantes cualquiera
c = 3
gamma = 1
w1 = 2
theta = 0

A = 1
B = 1.5
w = w1

#Defino las funciones numericas
def oscilador(t):
    return (
        c * np.exp((-gamma*t)/2) * np.cos(w1*t + theta) + A*np.cos(w*t) + B*np.sin(w*t)
        )

#Defino un set de tiempo
tiempo = np.arange(0, 200, 0.0001)

#Armo el grafico
plt.figure()
plt.plot(tiempo, oscilador(tiempo), linestyle='-', marker='None')
plt.xlabel('Tiempo')
plt.ylabel(r'$\psi$')
plt.title('Oscilador Armónico forzado')
plt.grid()
plt.show()
