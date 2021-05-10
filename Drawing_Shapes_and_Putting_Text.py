# series 3
import cv2 as cv
import numpy as np

# create a blank image
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# paint the image a certain color
blank[:] = 0,255,0 # green
#blank[:] = 0,0,255 # red

# certain area
blank[200:300,300:400] = 0,0,255 # red in blank (which is green here)
cv.imshow('Green', blank)

# draw rectangle
cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2) # point1 is the origin and the point2 is 250,250

# fill the rectangle
# cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=cv.FILLED) # point1 is the origin and the point2 is 250,250

# directly the mid point of the given img
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=cv.FILLED) # point1 is the origin and the point2 is 250,250

cv.imshow('Rectangle', blank)

# draw circle and fill it (cv.FILLED or -1, both okay)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,255), thickness=-1) # 40 pixels radius
cv.imshow('Circle', blank)

# draw a line
cv.line(blank, (450,450), (blank.shape[1]//2, blank.shape[0]//2), (255,225,225), thickness=3)
cv.imshow('Line', blank)

# write text
cv.putText(blank, 'Hello', (400,25), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2) # thickness, color, size
cv.imshow('Text', blank)

message = 'Can you hear me?'
cv.putText(blank, message, (330,50), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0,0,255), 2)
cv.imshow('Text message', blank)

# wait infinitely
cv.waitKey(0)