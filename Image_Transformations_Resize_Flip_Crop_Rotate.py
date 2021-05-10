# series 5
import cv2 as cv
import numpy as np

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

# -x -> left
# -y -> up
#  x -> right
#  y -> down

# right 100, down 100 pixels
translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# left 100, down 100 pixels
translated_2 = translate(img, -100, 100)
cv.imshow('translated_2', translated_2)

# rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width, height)

    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(img, 45)
# rotated = rotate(img, -45) # use "-" for reverse direction
cv.imshow('rotated', rotated)

# notice that the image is distorted, some of the pixels are lost
# it is possible to use nearest neighbor method
rotated_rotated = rotate(rotated, -45)
cv.imshow('rotated_back', rotated_rotated)

# resizing
resized = cv.resize(img, (1000,1000), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# flipping, use 0,1,-1 for horizontal, vertical, both
flipped = cv.flip(img, 0)
cv.imshow('flipped', flipped)

# cropping
cropped = img[50:450, 50:450]
cv.imshow('cropped', cropped)

cv.waitKey(0)