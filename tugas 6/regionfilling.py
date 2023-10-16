import cv2
import numpy as np

# Baca citra asli
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_COLOR)

# Salin citra asli ke citra target untuk dilakukan region filling
target_image = input_image.copy()

# Tentukan titik awal (seed) untuk region filling
seed_point = (100, 100)  # Koordinat (x, y) seed point

# Tentukan warna atau nilai yang akan digunakan untuk mengisi wilayah
fill_color = (0, 0, 255)  # Warna merah, bisa disesuaikan sesuai format (B, G, R)

# Buat elemen struktural (kernel) untuk operasi dilasi
kernel = np.ones((3, 3), np.uint8)

# Lakukan region filling menggunakan operasi dilasi
while True:
    prev_target_image = target_image.copy()
    target_image = cv2.dilate(target_image, kernel, anchor=seed_point, iterations=1)
    # Jika tidak ada perubahan pada citra target, proses selesai
    if (target_image == prev_target_image).all():
        break

# Tampilkan citra asli dan hasil region filling
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Region Filling', target_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
