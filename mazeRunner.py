import cv2
import numpy as np

img = cv2.imread('images/5.png')

cv2.imshow('Original image', img)
cv2.waitKey(0)

# Binary conversion
grayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(grayScale, 127, 255, cv2.THRESH_BINARY_INV)

# Contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
print "total contours : ", len(contours)
maxlen = 0
maxind = 0
for i in range(len(contours)):
	if len(contours[i])>maxlen:
		maxlen = len(contours[i])
		maxind = i
cv2.drawContours(thresh, contours, maxind, (255, 255, 255), -1)

cv2.imshow('Contour_nothresh', thresh)
cv2.waitKey(0)

# ret, thresh = cv2.threshold(thresh, 200, 255, cv2.THRESH_BINARY)
# ret, thresh = cv2.threshold(thresh, 220, 255, cv2.THRESH_BINARY)
ret, thresh = cv2.threshold(thresh, 240, 255, cv2.THRESH_BINARY)


cv2.imshow('Contour', thresh)
cv2.waitKey(0)

# Dilate
kernel = np.ones((20, 20), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations=1)

# cv2.imshow('Dil', dilation1)
# cv2.waitKey(0)

# dilation = cv2.dilate(dilation1, kernel, iterations=1)

cv2.imshow('Dil', dilation)
cv2.waitKey(0)

# Erosion
erosion = cv2.erode(dilation, kernel, iterations=1)

cv2.imshow('Ero', erosion)
cv2.waitKey(0)

diff = cv2.absdiff(dilation, erosion)


cv2.imshow('Diff', diff)
cv2.waitKey(0)

# splitting the channels of maze
b, g, r = cv2.split(img)
mask_inv = cv2.bitwise_not(diff)


cv2.imshow('Inv', mask_inv)
cv2.waitKey(0)

# masking out the green and red colour from the solved path
r = cv2.bitwise_and(r, r, mask=mask_inv)
g = cv2.bitwise_and(g, g, mask=mask_inv)

# r = 0
# g = 0

res = cv2.merge((b, g, r))
cv2.imshow('Solved Maze', res)

cv2.waitKey(0)
cv2.waitKey(0)
cv2.destroyAllWindows()
