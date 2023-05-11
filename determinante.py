import statistics
import time


# formula di Laplace
def calcolo_determinante(mat):
    n = len(mat)
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    det = 0
    for j in range(n):
        segno = (-1) ** (j + 2)  # perchè j parte da 0
        sotto_matrice = []
        for i in range(1, n):
            riga = []
            for k in range(n):
                if k != j:
                    riga.append(mat[i][k])
            sotto_matrice.append(riga)
        det += segno * mat[0][j] * calcolo_determinante(sotto_matrice)
    return det


if __name__ == '__main__':
    # defining matrix
    A = [[1, 4, 5, 5],
         [-5, 8, 9, 6],
         [6, -2, 1, 7],
         [6, -2, 1, 2]
         ]

    tempi = []
    for i in range(1000):
        inizio = time.time()
        calcolo_determinante(A)
        fine = time.time()
        tempo = fine - inizio
        tempi.append(tempo)

    tempo_medio = statistics.mean(tempi)
    print("Tempo di esecuzione medio per una matrice 8x8:", tempo_medio, "secondi")

