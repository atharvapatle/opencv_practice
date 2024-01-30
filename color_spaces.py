import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img=cv.imread("Photos\group 1.jpg")

# gray=cv.cvtColor(img,cv.COLOR_BGR2HSV_FULL)
# cv.imshow("gray",gray)

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("img",img)
plt.imshow(img)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()