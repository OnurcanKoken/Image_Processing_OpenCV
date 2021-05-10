# series 9
# averaging, gaussian, median, bilateral
import cv2 as cv

# read the image
img = cv.imread('photos/img_2.jpg')

# display the image
cv.imshow('assassins creed', img)

# averaging
average = cv.blur(img, (3,3))
cv.imshow('average', average)

# gaussian  - more natural compared to averaging
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian', gauss)

# median - less blurred in my opinion, seems like a bit better
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

# wait infinitely
cv.waitKey(0)