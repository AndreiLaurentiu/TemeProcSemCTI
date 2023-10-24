import numpy as np
import matplotlib.pyplot as plt
import sounddevice as snd
import time

def ex5():
    f1 = 240
    f2 = 400
    t = np.linspace(0, 0.01, 900)

    signal1 = 2 * (t * f1 - np.floor(0.5 + t * f1))
    signal2 = 2 * (t * f2 - np.floor(0.5 + t * f2))

    result = np.concatenate((signal1, signal2))

    snd.play(result, 44100)
    time.sleep(1.0)
    snd.stop()

# Sunetul rezultat este continuu si format din cele cele doua semnale in mod consecutiv