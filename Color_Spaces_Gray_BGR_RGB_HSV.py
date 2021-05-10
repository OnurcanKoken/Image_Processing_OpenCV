# series 7
# bgr, gray, hsv, matplotlib, rgb

import cv2 as cv
import matplotlib.pyplot as plt

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# convert grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray assassins creed', gray)

# convert HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv assassins creed', hsv)

# convert L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# using matplotlib
# instead of BGR, assumes the image as RGB
# plt.imshow(img)
# plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# using matplotlib
plt.imshow(rgb)
plt.show()

# note: to be able to convert gray to hsv: first convert to bgr, then hsv
# there might be a mistake, i did not searched about this situation

# wait infinitely
cv.waitKey(0)