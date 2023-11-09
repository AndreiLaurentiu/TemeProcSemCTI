import numpy as np
import matplotlib.pyplot as plt
import csv

def ex1():
    #a
    """
    In laborator spune ca a fost intervalul a fost de o ora, deci perioada de esantionare este de 1h (3600s)

    fs = 1 / T_s 
    fs = 1 / 3600
    fs ~= 2.77 * 10 ^ (-4) Hz
    """

    #b
    """
    calculam in felul urmator: numarul de esantioane * 1h = 18288 h
    """


    x = np.genfromtxt('Train.csv', delimiter=',',  skip_header=1)
    

    t = np.linspace(0, 18288, 18288)

    plt.figure(figsize=(10, 6))
    plt.plot(t, x[:, 2])
    plt.xlabel('Esantioane')
    plt.ylabel('Numar de masini')
    plt.grid()
    plt.show()

    #c
    """
    frec max se noteaza cu B si indeplineste relatia: 
    f_s > 2B
    2.77 * 10^(-4) > 2B 
    B < 1.385 * 10^(-4)
    deci valoarea pentru frec max este: 1.384 * 10^(-4)
    """
 

    #d
    X = np.fft.fft(x[:, 2])
    plt.figure(figsize=(10, 6))
    plt.plot(t[:len(t) // 2], abs(X[:len(X) // 2]))
    plt.xlabel('Esantioane')
    plt.ylabel('Numar de masini')
    plt.grid()
    plt.show()

    #g
    id = 0
 
    start = np.where(x[:, id] == 2300)[0][0]
    
    val_luna = x[start:start + 840]
    
    x_ = val_luna[:, 2]
    
    X = np.fft.fft(x_)
    
    t = np.arange(0, len(x_))
    
    plt.figure(figsize=(12, 6))
    plt.plot(t, abs(X))
    plt.xlabel('Esantionare')
    plt.ylabel('Nr masini')
    plt.show()


    #i
    x = x[:, 2]
    x = x[x < 5]
    X = np.fft.fft(x)
    t = np.arange(0, len(x))
    plt.figure(figsize=(10, 6))
    plt.plot(t, abs(X))
    plt.xlabel('Esantioane')
    plt.ylabel('Numar de masini')
    plt.grid()
    plt.show()
