import cv2
import numpy as np

# Baca citra biner
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Buat elemen struktural (strel)
kernel = np.ones((5, 5), np.uint8)  # Anda dapat mengganti ukuran kernel sesuai kebutuhan

# Lakukan dilasi
dilated_image = cv2.dilate(input_image, kernel, iterations=1)

# Simpan gambar hasil dilasi
cv2.imwrite('hasil_dilasi.png', dilated_image)

# Tampilkan citra asli dan hasil dilasi (opsional jika Anda ingin menampilkan)
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Dilasi', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
