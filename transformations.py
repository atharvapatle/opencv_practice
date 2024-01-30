import cv2 as cv
import numpy as np

img=cv.imread("Photos\park.jpg")

# Translation
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimension=(img.shape[1],img.shape[0])
#     return cv.warpAffine(img,transMat,dimension)

# -x -> left, +x -> right (shift)
# -y ->up , +y -> down (shift)

# translated=translate(img,65,-44)
# cv.imshow('',translated)

# Rotation
# def rotate(img,angle,point=None):
#     (height,width)=img.shape[:2]
#     if point is None:
#         point=(width//2,height//2)
#     rotMat=cv.getRotationMatrix2D(point,angle,1.0)
#     dimension=(width,height)

#     return cv.warpAffine(img,rotMat,dimension)

# rotated=rotate(img,33)  
# cv.imshow('',rotated)  



cv.waitKey(0)