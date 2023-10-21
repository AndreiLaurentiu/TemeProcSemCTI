import numpy as np
import matplotlib.pyplot as plt
import scipy
import sounddevice as sd

def ex3():
    rate = 44100

    t1 = np.linspace(0, 0.035, int(rate * 0.035))
    signal1 = np.sin(2 * np.pi * 400 * t1)

    t2 = np.linspace(0, 3, int(rate * 3))
    signal2 = np.sin(2 * np.pi * 800 * t2)

    t3 = np.linspace(0, 0.01, int(rate * 0.01))
    signal3 = 2 * (t3 * 240 - np.floor(0.5 + t3 * 240))

    t4 = np.linspace(0, 0.01, int(rate * 0.01))
    signal4 = np.sign(np.sin(2 * np.pi * 300 * t4))

    sd.play(signal1, rate)
    sd.wait()
    sd.play(signal2, rate)
    sd.wait()
    sd.play(signal3, rate)
    sd.wait()
    sd.play(signal4, rate)
    sd.wait()

    scipy.io.wavfile.write('signal1.wav', rate, signal1)

    _, signal1_wav = scipy.io.wavfile.read('signal1.wav')
    sd.play(signal1_wav, rate)
    sd.wait()