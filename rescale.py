import cv2

img = cv2.imread('assets/pic.jpg')

def rescaleFrame(frame, scale=0.55):
    width = int(frame.shape[1] * scale) #frame.shape[1] is the width of the origiinal image 
    height = int(frame.shape[0] * scale)#frmae.shape[0] is the original height of the image
    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)
    #cv2.resize just resizes our given image by first taking in the frame then the dimnesions for the new image and then the interpolation 


cv2.imshow('New image',rescaleFrame(img))
cv2.waitKey(0)