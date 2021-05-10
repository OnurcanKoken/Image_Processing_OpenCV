# köken
# 04.05.2021
# reference: https://www.etutorialspoint.com/index.php/320-how-to-capture-a-video-in-python-opencv-and-save
import cv2 as cv
import numpy as np
import time
# read the image
# img = cv.imread('photos/img_1.jpg')

# display the image
# cv.imshow('assassins creed', img)

# wait infinitely
# cv.waitKey(0)

# since there exist "cv.waitKey(0)" here
# after you close the window of photo on the screen
# video will be on the screen

# read the video
# capture = cv.VideoCapture('videos/deurov_1.mp4')
# capture = cv.VideoCapture('videos/output1.mp4')

# usb cam usage
# instead of "0", you might want to use your other cameras, for ex. "1"
capture = cv.VideoCapture(0)

# video recording
codec = cv.VideoWriter_fourcc(*'XVID')
#this can be used if you know your fps and width/height dimentions
#output = cv.VideoWriter('capture.avi', codec, 30, (640, 480))

recording_flag = False # recording variable
vid_i = 0 # count number of captured videos
cnt_i = 0 # count number of saved images

# used to calculate fps
prev_frame_time=0 # previous frame time
new_frame_time=0

# to be able to read videos frame by frame
# use while loop
while True:
    # frame by frame
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    key = cv.waitKey(1)

    # obtain the shape of the frame
    # this allows us to record the video with correct dimentions
    # otherwise, you wont be able to record
    # or you need to resize frame and insert that dimentions
    # into VideoWriter
    height, weight, channel = frame.shape

    # calculate fps
    new_frame_time = time.time()
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    fps = int(fps)

    # if you have problems with the calculations of fps
    # you can try the following line
    # # Get Frame Per Second
    # fps = capture.get(cv.CAP_PROP_FPS)

    # press "p" to save an image
    if cv.waitKey(1) & 0xFF == ord('p'):
        cv.imwrite("image%d.jpg" % cnt_i, frame)
        print("image saved - " + str(cnt_i))
        cnt_i = cnt_i + 1

    # record video if "space" is pressedqqqq
    elif key%256 == 32:
        if recording_flag == False:
            # transitioning from not recording to recording

            # you can record here by seperated files
            recorded_file_name = "capture_" + str(vid_i) + ".avi"
            output = cv.VideoWriter(recorded_file_name, codec, fps, (weight, height))
            print("recording video" + str(vid_i))
            vid_i = vid_i + 1

            # or just continue to write on the captured video
            #output.write(frame)
            #print("only recording on the same video")
            recording_flag = True
        else:
            # transitioning from recording to not recording
            print("stopped!")
            recording_flag = False

    # keep recording...
    if recording_flag:
        output.write(frame)

    # press "esc" to exit
    if key%256 == 27:
        break

    # or stop if 'q' is pressed
    if cv.waitKey(20) & 0xFF==ord('q'):
        break

capture.release()
# might cause error if you did not record any video
output.release()
cv.destroyAllWindows()



