import numpy as np
import matplotlib.pyplot as plt

def ex2():
    f = 5
    n = 800
    t = np.linspace(0, 2, n)
    x = np.sin(2 * np.pi * f * t)
    
    X = np.empty(n, dtype=complex)
    for i in range(n):
        X[i] = x[i] * np.e ** (-2 * np.pi * 1j * t[i])

    _, axs = plt.subplots(2)
    plt.suptitle('Semnal sinusoidal')
    axs[0].plot(t, x, 'g')
    axs[0].axhline(0, c='black')

    axs[1].scatter(X.real, X.imag, s=3, c=np.sqrt(X.real**2 + X.imag**2))
    axs[1].set_xlim([-1.2, 1.2])
    axs[1].set_ylim([-1.2, 1.2])
    axs[1].set_xlabel('Real')
    axs[1].set_ylabel('Imaginar')
    axs[1].set_aspect('equal', adjustable='box')

    plt.show()