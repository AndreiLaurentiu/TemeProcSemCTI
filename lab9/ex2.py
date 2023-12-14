import numpy as np
import matplotlib.pyplot as plt

def ex2():
    # a
    n = 1000
    x = np.arange(n)

    trend = -3 * x**2 + 15 * x - 2
    sezon = np.cos(2 * np.pi * 4 * x) + np.sin(2 * np.pi * 2 * x)
    res = np.random.rand(n)

    serie = trend + sezon + res

    s = np.empty(n)

    alfa = 0.75

    for i in range(n):
        sum = 0
        for j in range(i, i+1):
            sum += sum + ((1 - alfa)**(i-j)) * serie[j]
        s[i] = alfa * sum + ((1-alfa)**i)*serie[0]

    plt.figure(figsize=(12, 6))

    plt.plot(x, s, label="mediana")

    plt.plot(x, serie, label="original")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.show()

    