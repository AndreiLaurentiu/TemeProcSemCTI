import numpy as np
import cv2  # OpenCV for video handling
from scipy.fft import dctn, idctn
import os

def compress_frame(frame, jpeg_Q):
    jpeg_blocks = []

    for row in range(0, frame.shape[0], 8):
        for col in range(0, frame.shape[1], 8):
            square = frame[row:row+8, col:col+8]
            transformed = dctn(square)
            quantized = jpeg_Q * np.round(transformed / jpeg_Q)
            processed_block = idctn(quantized)
            jpeg_blocks.append(processed_block)

    rows_of_blocks = []
    for i in range(0, len(jpeg_blocks), frame.shape[1] // 8):
        row = np.hstack(jpeg_blocks[i:i + frame.shape[1] // 8])
        rows_of_blocks.append(row)
    
    compressed_frame = np.vstack(rows_of_blocks)
    return compressed_frame

def ex4():
    jpeg_Q = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                    [12, 12, 14, 19, 26, 58, 60, 55],
                    [14, 13, 16, 24, 40, 57, 69, 56],
                    [14, 17, 22, 29, 51, 87, 80, 62],
                    [18, 22, 37, 56, 68, 109, 103, 77],
                    [24, 35, 55, 64, 81, 104, 113, 92],
                    [49, 64, 78, 87, 103, 121, 120, 101],
                    [72, 92, 95, 98, 112, 100, 103, 99]])

    video_path = 'pexels_videos_1879456 (720p).mp4'

    cap = cv2.VideoCapture(video_path)

    frame_id = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        compressed_frame = compress_frame(gray, jpeg_Q)

        cv2.imwrite(os.path.join('.', f'frame_{frame_id:04d}.jpg'), compressed_frame)
        frame_id += 1

    cap.release()
