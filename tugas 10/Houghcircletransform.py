import cv2
import numpy as np

# Baca citra
image = cv2.imread('biner.jpeg', cv2.IMREAD_COLOR)

# Konversi citra ke grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Reduksi noise pada citra dengan Gaussian blur
gray = cv2.GaussianBlur(gray, (9, 9), 2)

# Deteksi lingkaran dengan Hough Circle Transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1,
                           minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        center = (i[0], i[1])
        cv2.circle(image, center, 1, (0, 100, 100), 3)
        radius = i[2]
        cv2.circle(image, center, radius, (0, 255, 0), 2)

# Tampilkan citra asli dan hasil deteksi lingkaran
cv2.imshow('Citra Asli', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
