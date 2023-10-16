import cv2
import numpy as np


def skeletonize(image):
    size = np.size(image)
    skel = np.zeros(image.shape, np.uint8)

    ret, img = cv2.threshold(image, 127, 255, 0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while not done:
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True

    return skel


# Baca citra biner
input_image = cv2.imread('biner.jpeg', cv2.IMREAD_GRAYSCALE)

# Lakukan skeletonization
skeleton_image = skeletonize(input_image)

# Tampilkan citra asli dan hasil skeletonization
cv2.imshow('Citra Asli', input_image)
cv2.imshow('Hasil Skeletonization', skeleton_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
