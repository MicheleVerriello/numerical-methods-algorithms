from random import random
import numpy as np
import matplotlib.pyplot as plot


def condizionamento_prodotto(n):
    # inizializzazione valori
    x = float(input("add value for x: "))
    y = float(input("add value for y: "))

    err_y = np.zeros(n)
    err_x = np.zeros(n)
    err_P = np.zeros(n)

    # creazione dati perturbati
    for i in range(n):
        xt = x + x * random() * 1.0 * np.e**-i
        yt = y + y * random() * 1.0 * np.e**-i

        # calcolo dei prodotti
        P = x * y
        Pt = xt * yt

        # calcolo errore sui dati
        err_x[i] = abs(x - xt) / abs(x)
        err_y[i] = abs(y - yt) / abs(y)
        err_P[i] = abs(P - Pt) / abs(P)

        print("Perturbazione: e**-%d" % i)
        print("Prodotto dei dati esatti: %f * %f = %.16f" % (x, y, P))
        print("Prodotto dei dati perturbati: %f * %f = %.16f" % (xt, yt, Pt))
        print("Errore sul dato x: %e: " % err_x[i])
        print("Errore sul dato y: %e: " % err_y[i])
        print("Errore sul prodotto P: %e: " % err_P[i])
        print(" ")

    return err_x, err_y, err_P


if __name__ == '__main__':
    n = 20
    errX, errY, errP = condizionamento_prodotto(n)

    # creazione plot
    plot.figure('Confronto tra errori sui dati e sui risultati')
    plot.grid()
    plot.semilogy(np.array(range(n)), errP, label="Errore sul prodotto", color="black")
    plot.semilogy(np.array(range(n)), errX, label="Errore su x", color="orange")
    plot.semilogy(np.array(range(n)), errY, "g-", label="Errore su y")
    plot.legend()
    plot.show()
