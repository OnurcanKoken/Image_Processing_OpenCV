# series 2
import cv2 as cv

# rescale the video by 75%
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# rescale an image
# read the image
img = cv.imread('photos/img_1.jpg')
# display the image
cv.imshow('assassins creed', img)
# resize the image
resized_img = rescaleFrame(img)
cv.imshow('Image', resized_img)

# read the video
capture = cv.VideoCapture('videos/deurov_1.mp4')

# to be able to read videos frame by frame
# use while loop
while True:
    # frame by frame
    isTrue, frame = capture.read()

    # default
    #frame_resized = rescaleFrame(frame)

    # instead of scaling 75%, scale 40%
    frame_resized = rescaleFrame(frame, scale = 0.4)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    # stop video if 'd' is pressed
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
