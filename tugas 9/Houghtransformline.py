import cv2
import numpy as np

# Baca citra
image = cv2.imread('biner.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Lakukan deteksi tepi menggunakan Canny
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Lakukan Probabilistic Hough Line Transform
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=10)

# Gambar garis yang terdeteksi pada citra
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

# Tampilkan citra asli dan hasil deteksi garis
cv2.imshow('Citra Asli', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
