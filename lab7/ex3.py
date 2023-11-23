from scipy import misc, ndimage
import numpy as np
import matplotlib.pyplot as plt

def ex3():

    X = misc.face(gray=True)
    
    pixel_noise = 250

    noise = np.random.randint(-pixel_noise, high=pixel_noise+1, size=X.shape)
    X_noisy = X + noise
    plt.imshow(X_noisy, cmap=plt.cm.gray)
    plt.title('Noisy')
    plt.show()
