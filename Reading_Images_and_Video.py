# series 1
import cv2 as cv

# read the image
img = cv.imread('photos/img_1.jpg')

# display the image
cv.imshow('assassins creed', img)

# wait infinitely
cv.waitKey(0)

# since there exist "cv.waitKey(0)" here
# after you close the window of photo on the screen
# video will be on the screen

# read the video
capture = cv.VideoCapture('videos/deurov_1.mp4')
#capture = cv.VideoCapture('videos/output1.mp4')

# usb cam usage
# capture = cv.VideoCapture(0)

# to be able to read videos frame by frame
# use while loop
while True:
    # frame by frame
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    # stop video if 'd' is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()



