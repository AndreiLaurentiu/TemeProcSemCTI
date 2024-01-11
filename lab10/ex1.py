import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal


def ex1():
    med = 0
    var = 0.3

    x = np.linspace(-2 * var, 2 * var)
    distGauss = (1 / var * np.sqrt(2 * np.pi)) * \
        np.exp(-(x - med) ** 2 / (2 * var))

    mat_cov = [[1, 3/5], [3/5, 2]]

    medie = [0, 0]

    mvn = multivariate_normal(medie, mat_cov)

    dG_bidimensionala = mvn.rvs(1000)

    plt.figure(figsize=(6, 10))
    plt.plot(x, distGauss, 'y')
    plt.xlabel('x')
    plt.ylabel('gamma')
    plt.title('Distributia Gaussiana')
    plt.grid()

    plt.figure(figsize=(6, 10))
    plt.scatter(dG_bidimensionala[:, 0], dG_bidimensionala[:, 1])

    plt.title('DG Bid')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    plt.show()
