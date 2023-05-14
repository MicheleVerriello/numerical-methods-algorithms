import numpy as np

# funzione da integrare
def f(x):
    # -6 * x ** 2 + 16 * x - 4 | 3 * np.exp(x) + 1
    return -6 * x ** 2 + 16 * x - 4

# primitiva
def F(x):
    # -2 * x ** 3 + 8 * x**2 - 4*x | 3 * np.exp(x) + x
    return -2 * x ** 3 + 8 * x**2 - 4*x

# intervallo di integrazione
a = 1.0
b = 2.0

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
