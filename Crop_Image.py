import cv2
img = cv2.imread("photos/img_1.jpg")
# left top point is the origin (0,0)
# ------------------> x increases
# |
# |
# |
# |
# |
# v
# y increases

x = 100
y = 100
w = 200 # width
h = 200 # height
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.imshow("original", img)
cv2.waitKey(0)

# reference: https://www.codegrepper.com/code-examples/python/crop+image+using+coordinates+python+opencv
# date 11th of May, 2021
# onurcan köken