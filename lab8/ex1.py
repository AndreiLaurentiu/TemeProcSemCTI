import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg


def ex1():
    #a
    n = 1000
    x = np.arange(n, dtype=np.float64)

    trend = -3 * x**2 + 15 * x - 2
    sezon = np.cos(2 * np.pi * 4 * x) + np.sin(2 * np.pi * 2 * x)
    res = np.random.rand(n)
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

    #b
    auto = np.correlate(serie, serie, mode='full')
    auto = auto[auto.size // 2:]
    plt.figure(2)
    plt.plot(x, auto, 'y')
    plt.title('Autocorelatie')
    plt.grid()

    #c
    p = 10
    model = AutoReg(serie, lags=p)
    model_fit = model.fit()

    prediction_length = 1000
    predictions = model_fit.predict(start=n, end=n + prediction_length - 1, dynamic=False)

    plt.figure(3)
    plt.title('Seria de timp și predicțiile sale')
    plt.plot(x, serie, 'black', label='Seria de timp')
    plt.plot(np.arange(n, n + prediction_length), predictions, 'red', label='Model AR')
    plt.legend()

    plt.show()



