from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

def ex1():

    #1
    n1 = 20
    n2 = 20

    X = np.empty((n1, n2))
    for i in range(n1):
        for j in range(n2):
            X[i][j] = np.sin(2 * np.pi * i + 3 * np.pi * j)

    plt.imshow(X, cmap=plt.cm.gray)
    plt.show()

    Y = np.fft.fft2(X)
    freq = 20 * np.log10(abs(Y))

    plt.imshow(freq)
    plt.show()

    #2
    X = np.empty((n1, n2))
    for i in range(n1):
        for j in range(n2):
            X[i][j] = np.sin(4 * np.pi * i) + np.cos(6 * np.pi * j)

    plt.imshow(X, cmap=plt.cm.gray)
    plt.show()

    Y = np.fft.fft2(X)
    freq = 20 * np.log10(abs(Y))

    plt.imshow(freq)
    plt.show()

    #3
    Y = np.zeros((n1, n2))
    Y[0][5] = 1
    Y[0][n2 - 5] = 1

    freq = 20 * np.log10(abs(Y))

    plt.imshow(freq)
    plt.show()

    X = np.fft.ifft2(Y)

    plt.imshow(X.real)
    plt.show()

    #4
    Y = np.zeros((n1, n2))
    Y[5][0] = 1
    Y[n2-5][0] = 1

    freq = 20 * np.log10(abs(Y))

    plt.imshow(freq)
    plt.show()

    X = np.fft.ifft2(Y)

    plt.imshow(X.real)
    plt.show()

    #5
    Y = np.zeros((n1, n2))
    Y[5][5] = 1
    Y[n2-5][n2-5] = 1

    freq = 20 * np.log10(abs(Y))

    plt.imshow(freq)
    plt.show()

    X = np.fft.ifft2(Y)

    plt.imshow(X.real)
    plt.show()








