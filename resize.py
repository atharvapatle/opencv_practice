import cv2 as cv

# Read the image
img = cv.imread('Photos/cat_large.jpg')

# Define the new resolution (width, height)
new_resolution = (800, 600)

# Resize the image
resized_img = cv.resize(img, new_resolution)

# Display the original and resized images
# cv.imshow('Original Cat', img)
cv.imshow('Resized Cat', resized_img)

cv.waitKey(0)
cv.destroyAllWindows()
