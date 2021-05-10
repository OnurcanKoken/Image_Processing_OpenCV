# series 10
import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('rectangle', rectangle)
cv.imshow('circle', circle)

# bitwise AND
# returns the intersection of the images
# 1's are on/white, 0's are off/black
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('bitwise AND', bitwise_and)

# bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('bitwise OR', bitwise_or)

# bitwise XOR
# returns the non-intersection of the images
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('bitwise XOR', bitwise_xor)

# bitwise NOT
# 0's -> 1's & 1's -> 0's
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise NOT', bitwise_not)

# wait infinitely
cv.waitKey(0)