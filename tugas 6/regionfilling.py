import cv2
import numpy as np

# Baca citra biner sebagai citra grayscale
input_image = cv2.imread('filling.jpg', cv2.IMREAD_GRAYSCALE)

# Salin citra asli ke citra target untuk region filling
target_image = input_image.copy()

# Tentukan titik awal (seed) untuk region filling
seed_point = (100, 100)  # Koordinat (x, y) seed point
target_value = 1  # Nilai yang akan digunakan untuk mengisi wilayah

def region_filling(image, seed, target_value):
    stack = [seed]

    while stack:
        current_seed = stack.pop()
        x, y = current_seed

        if x < 0 or x >= image.shape[1] or y < 0 or y >= image.shape[0]:
            continue

        if image[y, x] == target_value:
            continue

        image[y, x] = target_value

        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in neighbors:
            stack.append((x + dx, y + dy))

# Panggil fungsi region filling
region_filling(target_image, seed_point, target_value)

# Tampilkan citra asli dan hasil region filling
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Region Filling', target_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
