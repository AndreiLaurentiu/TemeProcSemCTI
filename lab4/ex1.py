import numpy as np
import matplotlib.pyplot as plt
import time

def ex1():

    N = [128, 256, 512, 1024, 2048, 4096, 8192]
    custom = []
    np_fft = []


    for val in N:
        t = np.linspace(0, 2, val)
        x = np.sin(2 * np.pi * t)
        start = time.time()
        F = np.array([[np.exp(2 * np.pi * 1j * m * n / val) for n in range(val)] for m in range(val)], dtype=complex)
        X = np.dot(F, x)
        end = time.time()
        custom.append(end - start)
        
        start = time.time()
        X = np.fft.fft(x)
        end = time.time()
        print(end - start)
        np_fft.append(end - start)


    plt.figure(figsize=(10, 6))
    plt.plot(N, custom, label='Custom', marker='*')
    plt.plot(N, np_fft, label='np.fft', marker='*')
    plt.yscale('log')
    #plt.xscale('log')
    plt.xlabel('N)')
    plt.ylabel('Execution Time (log scale)')
    plt.legend()
    plt.title('Comparison of DFT Implementations')
    plt.grid(True)
    plt.show()


