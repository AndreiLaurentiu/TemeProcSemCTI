import numpy as np
import matplotlib.pyplot as plt

def ex2():

    t = np.linspace(0, 1, 1000)

    fig, axs = plt.subplots(4)

    axs[0].plot(t, np.sin(2 * np.pi * 10 * t))

    fs = 21
    t_ = np.linspace(0, 1, fs)
    axs[1].plot(t, np.sin(2 * np.pi * 10 * t))
    axs[1].scatter(t_, np.sin(2 * np.pi * 10 * t_), c="gray")

    axs[2].plot(t, np.sin(2 * np.pi * 4 * t))
    axs[2].scatter(t_, np.sin(2 * np.pi * 4 * t_), c="green")

    axs[3].plot(t, np.sin(2 * np.pi * 6 * t))
    axs[3].scatter(t_, np.sin(2 * np.pi * 6 * t_), c="green")

    plt.tight_layout()
    plt.show()
