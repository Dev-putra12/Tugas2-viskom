import cv2
import numpy as np

# Baca citra biner sebagai citra grayscale
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Salin citra asli ke citra target untuk region filling
target_image = input_image.copy()

# Tentukan titik awal (seed) untuk region filling
seed_point = (100, 100)  # Koordinat (x, y) seed point
target_image[seed_point[1], seed_point[0]] = 1

# Buat elemen struktural (kernel) untuk operasi dilasi (strel simetrik)
kernel = np.array([[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]], np.uint8)

# Lakukan region filling menggunakan operasi dilasi dan interseksi
while True:
    prev_target_image = target_image.copy()
    dilated_image = cv2.dilate(target_image, kernel, iterations=1)
    target_image = np.minimum(dilated_image, input_image)
    # Jika tidak ada perubahan pada citra target, proses selesai
    if np.array_equal(target_image, prev_target_image):
        break

# Tampilkan citra asli dan hasil region filling
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Region Filling', target_image * 255)  # Mengecilkan hasil ke 0 dan 255
cv2.waitKey(0)
cv2.destroyAllWindows()
