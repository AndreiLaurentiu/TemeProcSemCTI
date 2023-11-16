import numpy as np
import matplotlib.pyplot as plt


def ex2():

    N = 2

    p = np.random.randint(-10, 10, N+1)  
    q = np.random.randint(-10, 10, N+1)  

    r = np.zeros(2 * N + 1)

    r = np.convolve(p, q)

    r2 = np.convolve(np.fft.fft(p), np.fft.fft(q))
    r2 = np.fft.ifft(r2)


    print(r)
    print(r2)





