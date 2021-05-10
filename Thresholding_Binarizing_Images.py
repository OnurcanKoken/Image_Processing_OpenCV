# series 13
import cv2 as cv

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# convert grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray assassins creed', gray)

# simple thresholding - 150 is the threshold variable here,
# over 1's, below 0's
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('simple thresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('simple inverse thresholded', thresh_inv)

# adaptive thresholding - GAUSSIAN or MEAN can be used
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive thresholded', adaptive_thresh)

# wait infinitely
cv.waitKey(0)
