# series 8
import cv2 as cv
import numpy as np

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# split the channels
b, g, r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

# 3 channels
print(img.shape)

# 1 channel of images
print(r.shape)
print(g.shape)
print(b.shape)

# get back the image
merged = cv.merge([b,g,r])
cv.imshow('merged', merged)

# colourful versions of each channel
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow('blueee', blue)
cv.imshow('greeen', green)
cv.imshow('reeeed', red)

# wait infinitely
cv.waitKey(0)