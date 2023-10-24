import numpy as np
import matplotlib.pyplot as plt

def ex7():
    f = 1000 
    t = np.linspace(0, 1, f)

    sina = np.sin(2 * np.pi * f * t)

    plt.figure(figsize=(12, 4))
    plt.subplot(3, 1, 1)
    plt.stem(t, sina)
    plt.title("Semnalul Initial")

    sindec = sina[::4]

    fdec = int(f / 4)

    tdec = np.linspace(0, 1, fdec)

    plt.subplot(3, 1, 2)
    plt.stem(tdec, sindec)
    plt.title("Semnalul Decimat")


    sindec2 = sina[1::4] # pornim de la elem 2 in vec

    plt.subplot(3, 1, 3)
    plt.stem(tdec, sindec2)
    plt.title("Semnal Decimat Pornind de la Al Doilea Element")

    plt.tight_layout()
    plt.show()
# a.)  in al doilea caz sunt mult mai putine puncte si intr-adevar functia pare discreta
# b.) asa cum am in acest moment pare ca graficele cu decimare la 1/4 sunt identice


