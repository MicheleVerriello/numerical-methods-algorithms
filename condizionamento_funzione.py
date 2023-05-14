from random import random
import numpy as np
import matplotlib.pyplot as plot


def condizionamento_radice(n):

    x = float(input("add value: "))

    # Inizializzazione dati
    xt = np.zeros(n)
    err_x = np.zeros(n)
    err_fx = np.zeros(n)
    fxt = np.zeros(n)
    fx = np.sqrt(x)

    # calcolo funzioni
    for i in range(n):
        xt[i] = x + x * random() * 1.0 * np.e ** -i
        fxt[i] = np.sqrt(xt[i])

        # calcolo errore
        err_x[i] = abs(x - xt[i]) / abs(x)
        err_fx[i] = abs(fx - fxt[i]) / abs(fx)

        print("Perturbazione: e**-%d" % i)
        print("Calcolo della funzione sul dato esatto: %.16f" % fx)
        print("Prodotto dei dati perturbati: %.16f" % fxt[i])
        print("Errore sul dato x: %e: " % err_x[i])
        print("Errore sulla funzione fx: %e: " % err_fx[i])
        print(" ")

    return err_x, err_fx


if __name__ == '__main__':
    n = 20
    errX, errFX = condizionamento_radice(n)

    # creazione plot
    plot.figure('Confronto tra errori sui dati e sui risultati')
    plot.grid()
    plot.semilogy(np.array(range(n)), errX, label="Errore su x", color="black")
    plot.semilogy(np.array(range(n)), errFX, label="Errore su fx", color="orange")
    plot.legend()
    plot.show()
