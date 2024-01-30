import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread("Photos\cats.jpg")
cv.imshow("Cat",img)

# Averaging
average=cv.blur(img,(5,5))
cv.imshow("Avg Blurr",average)

#Gaussian
gauss=cv.GaussianBlur(img,(5,5),0)
cv.imshow("Gaussian Blurr",gauss)

#median blur
median=cv.medianBlur(img,5)  #3 in place (3,3), 3 also accepted 
cv.imshow("median Blurr",median)

#bilateral blurring // apply the blurr, but retains the edges of the image 
bilat=cv.bilateralFilter(img,15,45,40)
cv.imshow("bilat Blurr",bilat)


cv.waitKey(0)
cv.destroyAllWindows()