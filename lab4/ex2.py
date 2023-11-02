import numpy as np
import matplotlib.pyplot as plt

def ex2():

    # Parametrii semnalului
    amplitudine = 1.0
    frecventa_originala = 10.0  # Hz
    frecventa_esantionare = 15.0  # Hz (sub-Nyquist)

    # Timpul de esantionare
    T = 1.0 / frecventa_esantionare
    t = np.arange(0, 1, T)

    # Semnalul sinusoidal original
    semnal_original = amplitudine * np.sin(2 * np.pi * frecventa_originala * t)

    # Esantionarea semnalului original
    semnal_esantionat = amplitudine * np.sin(2 * np.pi * frecventa_originala * t)

    # Plasarea pe aceeasi figura a semnalului original si a celui esantionat
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, semnal_original)
    plt.title('Semnal Original')

    plt.subplot(2, 1, 2)
    plt.plot(t, semnal_esantionat)
    plt.title('Semnal Esantionat cu frecventa sub-Nyquist')

    plt.tight_layout()
    plt.show()
