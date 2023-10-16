import cv2
import numpy as np

# Baca citra biner
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Buat elemen struktural (strel)
# Anda dapat mengganti ukuran kernel sesuai kebutuhan
kernel = np.ones((5, 5), np.uint8)

# Lakukan erosi
eroded_image = cv2.erode(input_image, kernel, iterations=1)

# Tampilkan citra asli dan hasil erosi
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Erosi', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
