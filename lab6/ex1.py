import numpy as np
import matplotlib.pyplot as plt

def ex1():

    N = 100
    x = np.random.rand(N)

    print(x)

    iteratii = [x]

    for i in range(3):
        x = np.convolve(x, x)
        iteratii.append(x)

    plt.figure(figsize=(16, 8))
    for i, iteratie in enumerate(iteratii):
        plt.subplot(2, 2, i + 1)
        plt.plot(iteratie)
        plt.title('Iter ' + str(i))
        plt.grid()

    plt.show()
