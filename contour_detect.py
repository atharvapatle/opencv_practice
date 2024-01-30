import cv2 as cv
import numpy as np


img = cv.imread("Photos\cats.jpg")
# cv.imshow('cat', img)

# Correct the color conversion constant
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('cat', gray)

# BLANK
blank=np.zeros(img.shape,dtype='uint8')

# blur=cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)


# canny=cv.Canny(blur,150,200)
# cv.imshow('cat', canny)

# Threshold
# 1. Input Image:
#    - `gray`: Grayscale image to be thresholded.

# 2. Thresholding:
#    - `cv.threshold(gray, 125, 255, cv.THRESH_BINARY)`: Converts pixel values; >125 to white, <=125 to black.

# 3. Output:
#    - `thresh`: Resulting binary image after thresholding.

# 4. Indicator:
#    - `ret`: Boolean indicating success (commonly used for debugging).
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
# cv.imshow("Thersh",thresh)


# Contours are essentially the boundaries of objects in an image.
# RETR_LIST means all the contours are retrieved and put in a list
# cv.CHAIN_APPROX_NONE: This parameter specifies the contour approximation method.
# means that all the boundary points of the contours will be stored.
contours,hierarchies=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

# Display contours on blank image
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow("black_cont",blank)

cv.waitKey(0)
cv.destroyAllWindows()
