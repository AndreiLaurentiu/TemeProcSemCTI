import numpy as np
import matplotlib.pyplot as plt

def ex2():
    A = 1.0
    f = 2.0  
    faze = [ 0.0, 0.5, 0.75, 1.0]
    snr = 0.1

    t = np.linspace(0, np.pi, 500)

    z = np.random.normal(0, 1, len(t))

    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)  
    plt.title('Semnale Sinusoidale')
    plt.xlabel('Timp')
    plt.ylabel('Amplitudine')
    plt.legend()

    for faza in faze:
        plt.plot(t, A * np.sin(2 * np.pi * f * t + faza))

    plt.subplot(2, 1, 2)  
    plt.title('Zgomot')
    plt.xlabel('Timp')
    plt.ylabel('Amplitudine')
    plt.legend()
    

    for faza in faze:
        x = A * np.sin(2 * np.pi * f * t + faza)
        gama = np.sqrt((np.linalg.norm(x) ** 2) / ( np.linalg.norm(z) ** 2 * snr ))
        snr = snr * 10
        plt.plot(t, x + gama * z)

    plt.show()


        
        