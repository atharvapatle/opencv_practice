import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# capture=cv.VideoCapture('Videos\dog.mp4')
# while True:
#     isTrue,frame=capture.read()
#     frame_resize=rescaleFrame(frame)
#     # cv.imshow('Video',frame)
#     cv.imshow('Video',frame_resize)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
img=rescaleFrame(img,0.3)
cv.imshow('Cat',img)
# Wait for a key event indefinitely (0 means wait until a key is pressed)
cv.waitKey(0)

# Destroy all OpenCV windows
cv.destroyAllWindows()
