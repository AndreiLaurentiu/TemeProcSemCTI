import numpy as np
import matplotlib.pyplot as plt


def ex1():
    # a
    n = 1000
    x = np.arange(n)

    trend = -3 * x**2 + 15 * x - 2
    sezon = np.cos(2 * np.pi * 4 * x) + np.sin(2 * np.pi * 2 * x)
    res = np.random.rand(n)

    trend *= 1e-4
    sezon *= 1e10

    serie = trend + sezon + res

    _, axs = plt.subplots(4, figsize=(10, 10))
    plt.suptitle('Serie de timp')

    axs[0].plot(x, serie, 'y')
    axs[0].set_ylabel('Serie')

    axs[1].plot(x, trend, 'b')
    axs[1].set_ylabel('Trend')

    axs[2].plot(x, sezon, 'r')
    axs[2].set_ylabel('Sezon')

    axs[3].plot(x, res, 'gray')
    axs[3].set_ylabel('Res')

    # b
    auto = np.correlate(serie, serie, mode='full')
    lags = np.arange(-n + 1, n)

    plt.figure(2)

    plt.plot(lags, auto, 'y')

    plt.title('Autocorelatie')
    plt.grid()

    # d

    plt.show()
