import cv2
import numpy as np

# Baca citra biner
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Buat elemen struktural (strel)
kernel = np.ones((5, 5), np.uint8)  # Anda dapat mengganti ukuran kernel sesuai kebutuhan

# Lakukan erosi
eroded_image = cv2.erode(input_image, kernel, iterations=1)

# Lakukan dilasi pada hasil erosi
opened_image = cv2.dilate(eroded_image, kernel, iterations=1)

# Tampilkan citra asli, hasil erosi, dan hasil opening
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Erosi', eroded_image)
cv2.imshow('Hasil Opening', opened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
