import numpy as np
import matplotlib.pyplot as plt

def ex2():
    # a
    f = 400
    n = 1600
    t = np.linspace(0, (n - 1) / f, n)
    signal = np.sin(2 * np.pi * f * t)

    plt.figure(figsize=(12, 8))
    plt.plot(t, signal)
    plt.title('Semnal sinusoidal de 400 Hz cu 1600 eșantioane')

    # b
    f = 800
    t = np.linspace(0, 3, int(3 * f))
    signal = np.sin(2 * np.pi * f * t)

    plt.figure(figsize=(12, 8))
    plt.plot(t, signal)
    plt.title('Semnal sinusoidal 800 Hz de 3 secunde')

    # c
    f = 240
    t = np.linspace(0, 1 - 1/f, int(f))
    signal = 2 * (t * f - np.floor(0.5 + t * f))

    plt.figure(figsize=(12, 8))
    plt.plot(t, signal)
    plt.title('Semnal sawtooth de 240 Hz')

    # d
    f = 300
    t = np.linspace(0, 1 - 1/f, int(f))
    signal = np.sign(np.sin(2 * np.pi * f * t))

    plt.figure(figsize=(12, 8))
    plt.plot(t, signal)
    plt.title('Semnal patrat de 300 Hz')

    # e
    signal = np.random.rand(128, 128)

    plt.figure(figsize=(12, 8))
    plt.imshow(signal, cmap='inferno')
    plt.title('Semnal 2D aleator de dim 128x128')

    # f
    signal = np.ones((128, 128))

    plt.figure(figsize=(12, 8))
    plt.imshow(signal, cmap='spring')
    plt.title('Semnal 2D de ones')

    plt.tight_layout()
    plt.show()
