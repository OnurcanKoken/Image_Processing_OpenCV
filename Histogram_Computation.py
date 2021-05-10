# series 12
import cv2 as cv
import matplotlib.pyplot as plt

# read the image
img = cv.imread('photos/img_3.jpg')

# display the image
cv.imshow('see', img)

# convert grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray see', gray)

# grayscale histogram
# insert list of images, which is only 1 image here
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# plot
# plt.figure()
# plt.title('grayscale histogram')
# plt.xlabel('bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# color histogram
# it is also possible to use a mask to focus on a certain area
plt.figure()
plt.title('color histogram')
plt.xlabel('bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

# wait infinitely
cv.waitKey(0)