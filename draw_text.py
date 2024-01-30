import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)
# blank[150:200,244:300]=255,0,0
# cv.rectangle(blank,(0,0),(250,350),(0,255,0),thickness=cv.FILLED)
cv.circle(blank,(250,250),98,(182,124,225),thickness=-1)
# cv.imshow('Green',blank)
cv.putText(blank,'Hello World',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,123),thickness=2)
cv.imshow('Text',blank)
cv.waitKey(0)