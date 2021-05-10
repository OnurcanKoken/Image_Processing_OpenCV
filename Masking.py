# series 11
import cv2 as cv
import numpy as np

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# create a blank image
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank', blank)

# create a white filled (-1 indicates that) circle at the mid point of the img with 100 pixels
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# or a rectangle
# mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
cv.imshow('mask', mask)

# use the mask and display the masked original image
# remember that the mask contains a white circle (1's)
# and bitwise operation takes the 1's only of the original image
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('masked', masked)

# what about  a half-moon masked image
blank_2 = np.zeros(img.shape[:2], dtype='uint8')
circle = cv.circle(blank_2.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank_2.copy(), (img.shape[1]//2, img.shape[0]//2 - 100), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
half_moon_mask = cv.bitwise_and(circle, rectangle)
half_moon_masked = cv.bitwise_and(img, img, mask=half_moon_mask)
cv.imshow('half-moon masked', half_moon_masked)

# wait infinitely
cv.waitKey(0)