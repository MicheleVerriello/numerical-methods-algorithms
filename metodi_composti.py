import numpy as np


# funzione da integrare
def f(x):
    # -6 * x ** 2 + 16 * x - 4 | 3 * np.exp(x) + 1
    return 3 * np.exp(x) + 1


# primitiva
def F(x):
    # -2 * x ** 3 + 8 * x**2 - 4*x | 3 * np.exp(x) + x
    return 3 * np.exp(x) + x


# formula trapezio composto
def trapezio_composto(f, a, b, N):
    x = np.linspace(a, b, N + 1)
    fx = f(x)
    S = 0
    for i in range(1, N):
        S = S + fx[i]
    TN = ((b - a) / (2 * N)) * (fx[0] + 2 * S + fx[N])
    return TN


def simpson_composto(f, a, b, N):
    # formula Cavalieri-Simpson
    z = np.linspace(a, b, N + 1)
    zz = []
    h = (z[1] - z[0]) / 2
    SN = 0
    zz.append(z[0])

    for i in range(1, N + 1):
        zz.append(h + z[i - 1])
        zz.append(z[i])

    z1 = np.array(zz)
    fz1 = f(z1)
    P = 0
    D = 0

    for i in range(1, len(z1), 2):
        D = fz1[i] + D
        if i == len(z1) - 2:
            break
        P = fz1[i + 1] + P
    SN = (fz1[0] + 4*D + 2*P + fz1[len(z1) - 1]) * h / 3
    return SN, z1, fz1


# intervallo di integrazione
a = 1.0
b = np.e

# calcolo integrale mediante formula composta
N = 3
TN = trapezio_composto(f, a, b, N)
SN, z1, fz1 = simpson_composto(f, a, b, N)

# calcolo errore commesso
I = F(b) - F(a)
E_T = abs(I - TN)
E_S = abs(I - SN)

# stampa risultati
print("Integrale esatto: %f" % I)
print("Formula trapezio (N=%3d): %f" % (N, TN))
print("Formula Simpson (N=%3d): %f" % (N, SN))
print("Errore commesso trapezio (N=%3d): %e" % (N, E_T))
print("Errore commesso Simpson (N=%3d): %e" % (N, E_S))
