import numpy as np
import matplotlib.pyplot as plt

def ex3():
    n = 800
    t = np.linspace(0, 1, n)
    fs = [63, 70, 90] # omega
    x = 0.9 * np.sin(2 * np.pi * fs[0] * t) + 0.7 * np.sin(2 * np.pi * fs[1] * t) + 2.35 * np.sin(2 * np.pi * fs[2] * t)

    X = np.empty(n, dtype=complex)
    for l in range(n):
        for i in range(n):
            X[l] += x[i] * np.e ** (-2 * np.pi * 1j * i * l / n)

    _, axs = plt.subplots(2)
    axs[0].plot(t, x)
    axs[0].set_xlabel('t')
    axs[0].set_ylabel('x')

    axs[1].stem(np.arange(n), np.sqrt(X.real**2 + X.imag**2), markerfmt='*', linefmt='red', basefmt=' ')
    axs[1].set_xlabel('Frecventa')
    axs[1].set_ylabel('Modul')

    

    plt.show()
