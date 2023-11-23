import numpy as np
import matplotlib.pyplot as plt

def ex4():

    # a
    x = np.genfromtxt('Train.csv', delimiter=',',  skip_header=1)
 
    start = np.where(x[:, 0] == 2300)[0][0]
    
    val_luna = x[start:start + 90]
    
    x_ = val_luna[:, 2]
    
    X = np.fft.fft(x_)
    
    t = np.arange(0, len(x_))

    # b
    w = [5, 9, 13, 17]

    plt.figure(figsize=(12, 6))

    for w_ in w:
        x_net = np.convolve(X, np.ones(w_), 'valid') / w_

        t = np.arange(0, len(x_net))

        
        plt.plot(t, x_net)

    plt.show()