import numpy as np
import matplotlib.pyplot as plot
from Lagrange import Lagrange

# funzione da integrare
def f(x):
    return 3 * np.exp(x) + 1

def F(x):
    return 3 * np.exp(x) + x

# intervallo di integrazione
a = 1
b = np.e

# calcolo formula del trapezio
T = (b - a)/2 * (f(a) + f(b))

# calcolo formula di simpson
S = ((b - a) / 6) * (f(a) + 4 * f(((a + b) / 2)) + f(b))

# calcolo errore commesso
I = F(b) - F(a)
E_T = abs(I - T)
E_S = abs(I - S)

# stampa risultati
print("Integrale esatto: %f" % I)
print("Formula trapezio: %f" % T)
print("Formula Simpson: %f" % S)
print("Errore commesso trapezio: %e" % E_T)
print("Errore commesso Simpson: %e" % E_S)

# rappresentazione grafica
x = np.linspace(a - 0.2, b + 0.2, 200)
x_int = np.linspace(a, b, 3)
fx = f(x)
xn = np.linspace(a, b, 100)
yn = f(xn)
px = Lagrange(xn, yn, x_int)
plot.figure(1)
plot.plot(x, fx, "k-", label="f(x)")
xx = np.array([a, a, b, b, a])
yy = np.array([0, f(a), f(b), 0, 0])
plot.plot(x_int, px, "g-", label="Simpson")
plot.plot(xx, yy, "b-", label="Trapezio")
plot.xlabel("x")
plot.legend()
