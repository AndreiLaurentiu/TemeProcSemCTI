import numpy as np
import matplotlib.pyplot as plt

def ex1():
    A = 1.0
    f = 2.0  
    faza = 0.0  

    t = np.linspace(0, np.pi, 500)

    sin = A * np.sin(2 * np.pi * f * t + faza)

    cos = A * np.cos(2 * np.pi * f * t + faza - np.pi / 2)


    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)  
    plt.plot(t, sin)
    plt.title('Semnal Sinusoidal')
    plt.xlabel('Timp')
    plt.ylabel('Amplitudine')
    plt.legend()

    plt.subplot(2, 1, 2)  
    plt.plot(t, cos)
    plt.title('Semnal Cosinusoidal Modificat')
    plt.xlabel('Timp')
    plt.ylabel('Amplitudine')
    plt.legend()
    
    plt.show()


