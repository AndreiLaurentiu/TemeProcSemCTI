import numpy as np
import matplotlib.pyplot as plt

def ex6():

    f = 900
    t = np.linspace (0, 1, 300)

    f_a = f / 2
    f_b = f / 4
    f_c = 0

    sin1 = np.sin(2 * np.pi * f_a * t)
    sin2 = np.sin(2 * np.pi * f_b * t)
    sin3 = np.sin(2 * np.pi * f_c * t)

    fig, axs = plt.subplots(3)
    fig.suptitle('Semnalele')
    axs[0].plot(t, sin1)
    axs[1].plot(t, sin2)
    axs[2].plot(t, sin3)

    plt.show()

# Atunci cand frecventa fundamentala scade, forma astepatata a sinusului devine liniara. Practic curbele periodice devin o linie