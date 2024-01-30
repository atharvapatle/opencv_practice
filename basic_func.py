import cv2 as cv
import numpy as np

img = cv.imread("Photos/group 2.jpg")

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

#Blur
blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)

# Edge cascade
canny=cv.Canny(blur,160,200)
# cv.imshow('Blur',canny)

#Dilate the image
dilate=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Blur',dilate)

#eroding
erode=cv.dilate(dilate,(3,3),iterations=1)
cv.imshow('Blur',erode)

# resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Blur',resized)

cv.waitKey(0)
cv.destroyAllWindows()
