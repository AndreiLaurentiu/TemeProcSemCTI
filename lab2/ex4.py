import numpy as np
import matplotlib.pyplot as plt

def ex4():
    #sawtooth
    f = 240
    t = np.linspace(0, 0.01, 900)
    signal1 = 2 * (t * f - np.floor(0.5 + t * f))

    #square
    f = 300
    t = np.linspace(0, 0.01, 900)
    signal2 = np.sign(np.sin(2 * np.pi * f * t))

    sum = signal1 + signal2

    fig, axs = plt.subplots(3)
    fig.suptitle('Semnalele')
    axs[0].stem(t, signal1)
    axs[1].stem(t, signal2)
    axs[2].stem(t, sum)

    plt.show()
