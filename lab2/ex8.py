import numpy as np
import matplotlib.pyplot as plt

def ex8():

    f = 100
    t = np.linspace(-np.pi / 2, np.pi / 2, f)

    sin = np.sin(t)

    sin_approx_t = t

    sin_approx_p = (t - (7 * t ** 3) / 60) / (1 + (t ** 2) / 20)

    err_t = sin - sin_approx_t
    err_p = sin - sin_approx_p

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 1, 1)
    plt.plot(t, sin, label='sin')
    plt.plot(t, sin_approx_t, label='aprox taylor')
    plt.plot(t, sin_approx_p, label='aprox pade')
    plt.title('Aproximarea sin in [-π/2, π/2]')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.semilogy(t, abs(err_t), label='taylor')
    plt.semilogy(t, abs(err_p), label='pade)')
    plt.title('Eroarea ca functie logaritmica')
    plt.legend()

    plt.tight_layout()
    plt.show()
