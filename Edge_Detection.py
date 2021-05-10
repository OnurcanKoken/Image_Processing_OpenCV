# series 14
import cv2 as cv
import numpy as np

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# convert grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray assassins creed', gray)

# laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

# sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('sobel x', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('combined sobel', combined_sobel)

# canny - edge cascade
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)

# wait infinitely
cv.waitKey(0)