import numpy as np
import matplotlib.pyplot as plot
import lagrange


def interpolazione_polinomiale(x, y, ordine):

    n = len(x)
    if ordine >= n:
        ordine = n - 1
    a = [0] * (ordine + 1)
    for j in range(ordine + 1):
        a[j] = y[j]
        for i in range(j - 1, -1, -1):
            a[i] = (a[i + 1] - a[i]) / (x[j] - x[i])

    def f(t):
        result = a[ordine]
        for i in range(ordine - 1, -1, -1):
            result = result * (t - x[i]) + a[i]
        return result

    return f


def calcolo_coeff_newton(xn, yn):
    a = np.copy(yn)
    n = len(xn)
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            a[i] = (a[i] - a[i - 1]) / (xn[i] - xn[i - j])
    return a


def newton_diff_div(d, xn, x):
    n = len(d) - 1
    P = d[n]
    for i in range(n - 1, -1, -1):
        P = d[i] + P * (x - xn[i])

    return P


def funz(x):
    y = x ** 2 + np.cos(2 * x)
    return y


# dati di interpolazione
a = -np.pi
b = np.pi
n = 60  # grado del polinomio
xn = np.linspace(a, b, n + 1)
yn = funz(xn)

V = [[xn[i] ** j for j in range(n + 1)] for i in range(n + 1)]
c = np.linalg.solve(V, yn)

# calcolo funzione e polinomio di interpolazione
x = np.linspace(a, b, 200)
fx = funz(x)
# px_l = interpolazione_polinomiale(xn, yn, x)
d = calcolo_coeff_newton(xn, yn)
px_n = newton_diff_div(d, xn, x)
px_ci = np.polyval(np.flipud(c), x)

# grafico funzione e polinomio
plot.figure(1)
plot.plot(x, fx, "b-", label="f(x)")
plot.plot(x, px_n, "o-", label="pn_n(x)")
# plot.plot(x, px_l, "g-", label="pn_l(x)")
plot.plot(x, px_ci, "r-", label="pn_ci(x)")
# plot.plot(xn, fx, "ro")
plot.xlabel("x")
plot.legend()
plot.show()

# grafico del resto
plot.figure(2)
plot.semilogy(x, abs(fx - px_n), "b-", label="|f(x) - pn_n(x)|")
# plot.semilogy(x, abs(fx - px_l), "g-", label="|f(x) - pn_l(x)|")
plot.semilogy(x, abs(fx - px_ci), "r-", label="|f(x) - pn_ci(x)|")
plot.xlabel("x")
plot.legend()
plot.show()
