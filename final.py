import cv2
import numpy as np

# Baca citra biner
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Tugas Pertama: Dilasi
def dilate_image(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    return dilated_image

# Tugas Kedua: Erosi
def erode_image(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    eroded_image = cv2.erode(image, kernel, iterations=1)
    return eroded_image

# Tugas Ketiga: Opening
def open_image(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opened_image

# Tugas Keempat: Closing
def close_image(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closed_image

# Lakukan Closing
closed_image = close_image(input_image, 3)

# Tugas Kelima: Transformasi Hit or Miss
def hit_or_miss_transform(image, kernel_hit, kernel_miss):
    result = cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel_hit)
    result_miss = cv2.morphologyEx(image, cv2.MORPH_HITMISS, kernel_miss)
    return cv2.bitwise_and(result, cv2.bitwise_not(result_miss))

# Tugas Keenam: Region Filling
def region_filling(image, seed_point):
    filled_image = image.copy()
    h, w = filled_image.shape
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(filled_image, mask, seed_point, 255)
    return filled_image

# Tugas Ketujuh: Thinning
def thinning(image):
    size = np.size(image)
    skel = np.zeros(image.shape, np.uint8)
    ret, img = cv2.threshold(image, 127, 255, 0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False
    while not done:
        prev_target_image = img.copy()
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()
        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True
    return skel

# Tugas Kelapan: Skeletonization
skeleton_image = thinning(closed_image)

# Tugas Kesembilan: Probabilistic Hough Line Transform
lines = cv2.HoughLinesP(skeleton_image, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=10)

# Tugas Sepuluh: Hough Circle Transform
circles = cv2.HoughCircles(skeleton_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=0, maxRadius=0)

# Menampilkan citra hasil setelah semua operasi
cv2.imshow('Hasil Dilasi', dilate_image(input_image, 5))
cv2.imshow('Hasil Erosi', erode_image(input_image, 5))
cv2.imshow('Hasil Opening', open_image(input_image, 5))
cv2.imshow('Hasil Closing', closed_image)
cv2.imshow('Hasil Hit or Miss Transform', hit_or_miss_transform(input_image, np.array([[0, 1, 0], [0, 1, 1], [0, 0, 0]], np.uint8), np.array([[0, 0, 0], [0, 1, 0], [0, 1, 0]], np.uint8)))
cv2.imshow('Hasil Region Filling', region_filling(closed_image, (100, 100)))
cv2.imshow('Hasil Thinning', skeleton_image)
cv2.imshow('Hasil Probabilistic Hough Line Transform', skeleton_image)
cv2.imshow('Hasil Hough Circle Transform', skeleton_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
