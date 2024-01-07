import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from scipy.fft import dctn, idctn

# cele 2 functii sunt folosite pt a converti intre RGB si YCbCr si invers
# formule preluate de aici: https://en.wikipedia.org/wiki/YCbCr#R'G'B'_to_Y%E2%80%B2PbPr
def rgb2ycbcr(img):
    Y = 0.299 * img[:,:,0] + 0.587 * img[:,:,1] + 0.114 * img[:,:,2]
    Cb = -0.168736 * img[:,:,0] - 0.331264 * img[:,:,1] + 0.5 * img[:,:,2] + 128
    Cr = 0.5 * img[:,:,0] - 0.418688 * img[:,:,1] - 0.081312 * img[:,:,2] + 128
    return np.round(np.stack((Y, Cb, Cr), axis=2)).astype(np.uint8)


def ycbcr2rgb(img):
    Y = img[:,:,0]
    Cb = img[:,:,1]
    Cr = img[:,:,2]
    R = Y + 1.402 * (Cr - 128)
    G = Y - 0.344136 * (Cb - 128) - 0.714136 * (Cr - 128)
    B = Y + 1.772 * (Cb - 128)
    RGB = np.stack((R, G, B), axis=2)
    # ne asiguram folosind clip ca este in intervalul 0 255
    return np.round(np.clip(RGB, 0, 255)).astype(np.uint8) 

def compress_channel(channel_data, quantization_matrix):
    # compresam pe rand un canal folosind DCT si cuantizare, similar cu ex1
    compressed_blocks = []
    for i in range(0, channel_data.shape[0], 8):
        for j in range(0, channel_data.shape[1], 8):
            block = channel_data[i:i+8, j:j+8]
            dct_block = dctn(block)
            quantized_block = quantization_matrix * np.round(dct_block / quantization_matrix)
            idct_block = idctn(quantized_block)
            compressed_blocks.append(idct_block)
    return np.block([compressed_blocks[i:i+channel_data.shape[1]//8] for i in range(0, len(compressed_blocks), channel_data.shape[1]//8)])

def ex2():
    X = misc.face()

    X_ycbcr = rgb2ycbcr(X)

     # matrice de cuantizare jpeg - Y
    quantization_Y = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                        [12, 12, 14, 19, 26, 28, 60, 55],
                        [14, 13, 16, 24, 40, 57, 69, 56],
                        [14, 17, 22, 29, 51, 87, 80, 62],
                        [18, 22, 37, 56, 68, 109, 103, 77],
                        [24, 35, 55, 64, 81, 104, 113, 92],
                        [49, 64, 78, 87, 103, 121, 120, 101],
                        [72, 92, 95, 98, 112, 100, 103, 99]])

    # matrice de cuantozare pt CbCr
    # valoare preluat de la urmatorul link: https://www.freecodecamp.org/news/how-jpg-works-a4dbd2316f35/
    quantization_CbCr = np.array([[17, 18, 24, 47, 99, 99, 99, 99],
                            [18, 21, 26, 66, 99, 99, 99, 99],
                            [24, 26, 56, 99, 99, 99, 99, 99],
                            [47, 66, 99, 99, 99, 99, 99, 99],
                            [99, 99, 99, 99, 99, 99, 99, 99],
                            [99, 99, 99, 99, 99, 99, 99, 99],
                            [99, 99, 99, 99, 99, 99, 99, 99],
                            [99, 99, 99, 99, 99, 99, 99, 99]])


     # compresam fiecare canal individual
    compressed_channels = [compress_channel(X_ycbcr[:,:,ch], quantization_Y if ch == 0 else quantization_CbCr) for ch in range(3)]

    # reunim canalele pt a obtine imaginea
    compressed_image = np.stack(compressed_channels, axis=2)

    plt.subplot(1, 3, 1)
    plt.imshow(X)
    plt.title('Original')

    plt.subplot(1, 3, 2)
    plt.imshow(X_ycbcr)
    plt.title('YCbCr')

    plt.subplot(1, 3, 3)
    plt.imshow(ycbcr2rgb(compressed_image))
    plt.title('Compresat')

    plt.show()

    