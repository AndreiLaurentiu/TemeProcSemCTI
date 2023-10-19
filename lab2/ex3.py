import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def ex3():
    f = 400
    n = 1600
    t = np.linspace(0, (n - 1) / f, n)
    signal = np.sin(2 * np.pi * f * t)

    sd.play(semnal_sinus, frecventa)
    sd.wait()

    nume_fisier_wav = "semnal_sinus.wav"
    wavfile.write(nume_fisier_wav, 1, signal)

    rate, semnal_incarcat = wavfile.read(nume_fisier_wav)

    if np.array_equal(semnal_sinus, semnal_incarcat):
        print("Semnalul a fost încărcat corect.")
    else:
        print("Semnalul încărcat nu corespunde cu semnalul generat.")