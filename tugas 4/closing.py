import cv2
import numpy as np

# Baca citra biner
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Buat elemen struktural (strel)
kernel = np.ones((5, 5), np.uint8)  # Anda dapat mengganti ukuran kernel sesuai kebutuhan

# Lakukan dilasi
dilated_image = cv2.dilate(input_image, kernel, iterations=1)

# Lakukan erosi pada hasil dilasi
closed_image = cv2.erode(dilated_image, kernel, iterations=1)

# Tampilkan citra asli, hasil dilasi, dan hasil closing
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Dilasi', dilated_image)
cv2.imshow('Hasil Closing', closed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
