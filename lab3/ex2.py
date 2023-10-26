import numpy as np
import matplotlib.pyplot as plt

def ex2():
    N = 10 

    t = np.linspace(0, 1, N)
    x = np.sin(2 * np.pi * 100 * t)

    y = np.array([[np.exp(2 * np.pi * 1j * m * n / N) for n in range(N)] for m in range(N)], dtype=complex) * x

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    ax1.plot(t, x)
    ax1.set_xlabel('Timp (s)')
    ax1.set_ylabel('Amplitudine')
    ax1.set_title('Semnal Sinusoidal')

    ax2.plot(np.real(y), np.imag(y))
    ax2.set_xlabel('Re(y[n])')
    ax2.set_ylabel('Im(y[n])')
    ax2.set_title('Cercul Unitate')

    plt.tight_layout()
    plt.show()

    