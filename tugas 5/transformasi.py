import cv2
import numpy as np

# Baca citra biner
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Buat elemen struktural untuk pola Hit
kernel_hit = np.array([[0, 1, 0],
                      [1, -1, 1],
                      [0, 1, 0]], dtype=np.int8)

# Buat elemen struktural untuk pola Miss
kernel_miss = np.array([[1, 0, 1],
                       [0, 1, 0],
                       [1, 0, 1]], dtype=np.int8)

# Lakukan transformasi Hit or Miss
hitmiss_result = cv2.morphologyEx(
    input_image, cv2.MORPH_HITMISS, kernel_hit, borderType=cv2.BORDER_CONSTANT, borderValue=(0))

# Tampilkan citra asli dan hasil transformasi Hit or Miss
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Transformasi Hit or Miss', hitmiss_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
