# series 4
# gray, blur, edge cascade, dilating/eroding, resizing/cropping
import cv2 as cv

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# convert grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray assassins creed', gray)

# blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('blur assassins creed', blur)

# edge cascade
canny = cv.Canny(img, 125,175)
cv.imshow('canny edges assassins creed', canny)

# to be able to decrease the number of edges, use blur
more_blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
blur_canny = cv.Canny(more_blur, 125,175)
cv.imshow('blur canny edges assassins creed', blur_canny)

# dilating the image
dilated = cv.dilate(blur_canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

# eroding the image (reverse dilating operation)
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('eroded', eroded)

# resize
# for enlarging an image: cv.INTER_CUBIC or cv.INTER_LINEAR
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

# crop
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)

# wait infinitely
cv.waitKey(0)