import numpy as np
import matplotlib.pyplot as plt

def ex1():
    N = 8
    t = np.linspace(0, 2, N)
    #x = np.sin(2 * np.pi * t)
    
    F = np.array([[np.exp(2 * np.pi * 1j * m * n / N) for n in range(N)] for m in range(N)], dtype=complex)

    fig, axs = plt.subplots(N, 2, figsize=(10, 8))
    fig.suptitle('Partea imaginara/ Reala')

    for i, ax_row in enumerate(axs):
        ax_row[0].plot(range(N), np.real(F[i]), 'g')
        ax_row[1].plot(range(N), np.imag(F[i]), 'r')
    
    #if abs(np.dot(F, F.conj().T) - N * np.identity(N)) <= 0.001:
    if np.allclose(np.dot(F, F.conj().T), N * np.identity(N), atol=0.001):
        print("Da")
    else:
        print("Nu")

    plt.show()
