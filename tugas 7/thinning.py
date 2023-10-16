import cv2
import numpy as np

# Baca citra biner
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Inisialisasi citra hasil dengan citra asli
thinning_image = input_image.copy()

# Tentukan kernel untuk operasi Thinning
kernel = np.array([[0, 0, 0],
                   [1, 1, 0],
                   [1, 1, 1]], dtype=np.uint8)

# Iterasi untuk melakukan Thinning
while True:
    prev_thinning_image = thinning_image.copy()
    thinning_image = cv2.morphologyEx(
        thinning_image, cv2.MORPH_HITMISS, kernel)
    # Jika tidak ada perubahan pada citra tipis, proses selesai
    if (thinning_image == prev_thinning_image).all():
        break

# Tampilkan citra asli dan hasil Thinning
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Thinning', thinning_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
