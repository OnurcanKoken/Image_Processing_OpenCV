# series 6
import cv2 as cv
import numpy as np

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# convert grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray assassins creed', gray)

# edge cascade
canny = cv.Canny(gray, 125,175)
cv.imshow('canny edges gray assassins creed', canny)

# list of counters -> counters
# counters inside counters -> hierarchies
counters, hierarchies = cv.findContours(gray, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print('canny_gray')
print(f'{len(counters)} counter(s) found!')

# blur (to be able to reduce the number of counters)
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur assassins creed', blur)

# edge cascade
canny = cv.Canny(blur, 125,175)
cv.imshow('canny edges blur assassins creed', canny)

counters, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print('canny_blur')
print(f'{len(counters)} counter(s) found!')

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thresh assassins creed', thresh)
# counters, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print('thresh')
# print(f'{len(counters)} counter(s) found!')

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.drawContours(blank, counters, -1, (0,0,255), 1)
cv.imshow('counters drawn', blank)
# wait infinitely
cv.waitKey(0)