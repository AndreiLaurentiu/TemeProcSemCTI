import numpy as np
import matplotlib.pyplot as plt

def ex3():

    t = np.linspace(0, 1, 200)
    x = np.sin(2 * np.pi * 100 * t)

    plt.figure(1)

    plt.plot(t, x)
    plt.plot(t, x * np.repeat([1], len(x)))
    plt.plot(t, x * 0.5 * (1 - np.cos(2 * np.pi * x / len(x))))

    plt.grid()

    plt.show()
