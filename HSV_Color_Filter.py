import cv2
import numpy as np


def nothing(x):
    pass

frame = cv2.imread('path/img.JPG')

print('Original Dimensions : ', frame.shape)
scale_percent = 60  # percent of original size
width = int(frame.shape[1] * scale_percent / 100)
height = int(frame.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)

cv2.namedWindow("HSV Value", cv2.WINDOW_NORMAL)
cv2.createTrackbar("H MIN", "HSV Value", 0, 179, nothing)
cv2.createTrackbar("H MAX", "HSV Value", 0, 179, nothing)
cv2.createTrackbar("S MIN", "HSV Value", 0, 255, nothing)
cv2.createTrackbar("S MAX", "HSV Value", 0, 255, nothing)
cv2.createTrackbar("V MIN", "HSV Value", 0, 255, nothing)
cv2.createTrackbar("V MAX", "HSV Value", 0, 255, nothing)

while(1):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # change the hsv limits upper and lower bounds
    h_min = cv2.getTrackbarPos("H MIN", "HSV Value")
    s_min = cv2.getTrackbarPos("S MIN", "HSV Value")
    v_min = cv2.getTrackbarPos("V MIN", "HSV Value")
    h_max = cv2.getTrackbarPos("H MAX", "HSV Value")
    s_max = cv2.getTrackbarPos("S MAX", "HSV Value")
    v_max = cv2.getTrackbarPos("V MAX", "HSV Value")

    lower_bound = np.array([h_min, s_min, v_min])
    upper_bound = np.array([h_max, s_max, v_max])

    print(h_min, lower_bound)
    hsv_min="MIN H:{} S:{} V:{}".format(h_min,s_min,v_min)
    hsv_max = "MAX H:{} S:{} V:{}".format(h_max, s_max, v_max)

    # masking operation
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.putText(result, hsv_min, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(result, hsv_max, (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("HSV Value", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Frame Mask", result)

    # for changing the range
    q = cv2.waitKey(1) & 0xFF
    if q == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()