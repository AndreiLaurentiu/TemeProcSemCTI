import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.fft import dctn, idctn

def ex1():
    # matrice de cuantizare jpeg
    jpeg_Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                       [12, 12, 14, 19, 26, 58, 60, 55],
                       [14, 13, 16, 24, 40, 57, 69, 56],
                       [14, 17, 22, 29, 51, 87, 80, 62],
                       [18, 22, 37, 56, 68, 109, 103, 77],
                       [24, 35, 55, 64, 81, 104, 113, 92],
                       [49, 64, 78, 87, 103, 121, 120, 101],
                       [72, 92, 95, 98, 112, 100, 103, 99]])

    # lista in care tinem toate rezultatele de la fiecare portinue 8 x 8
    jpeg_blocks = []

    # citim imaginea
    X = misc.ascent()

    # iteram prin fiecare bloc
    for row in range(0, X.shape[0], 8):
        for col in range(0, X.shape[1], 8):
            # extragem fiecare portiune 8 x 8
            square = X[row:row+8, col:col+8]
            # aplicam DCT
            transformed = dctn(square)
            # cuantizam jpeg
            quantized = jpeg_Q * np.round(transformed / jpeg_Q)
            # aplicam inversa DCT
            processed_block = idctn(quantized)
            jpeg_blocks.append(processed_block)

    # refacem imaginea unind patratele rezultate
    rows_of_blocks = []

    # iteram prin fiecare rand de patrate 8 x 8 din imaginea initiala
    for i in range(0, len(jpeg_blocks), X.shape[1] // 8):
        row = np.hstack(jpeg_blocks[i:i + X.shape[1] // 8])
        rows_of_blocks.append(row)

    # concantenam vertical randurile de patrate pt a forma imaginea initiala
    reconstructed_image = np.vstack(rows_of_blocks)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(X, cmap='gray')
    plt.title('Original')

    plt.subplot(1, 2, 2)
    plt.imshow(reconstructed_image, cmap='gray')
    plt.title('Compresat')

    plt.show()
