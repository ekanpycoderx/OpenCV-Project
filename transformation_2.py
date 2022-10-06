import cv2
import numpy as np
import sys

img = cv2.imread('assets/pic.jpg')

# Roatation of an image
def roatate(img, angle, rotPoint=None): #rotPoint is the roatation point aoround which the image will roatate based on the given angle to the function
    (height, width) = img.shape[:2] #Basically we are taking the hegiht and idth of the image by just grabbing the first 2 values from img.shape[]

    if rotPoint is None:
        rotPoint = (width//2, height//2) #This means our object will rotate aroung the centre of the image

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 0.5) #This is creating the roatation matrix we get like in the translation matrix in transformation.py file
    dimensions = (width,height) #1.0 is the scale value in the above statement mentioned which is the scle of the image

    return cv2.warpAffine(img, rotMat, dimensions)

roatated = roatate(img, 45)#It will do a anit-clockwise roation, for reversing the direction of rotation just specify the angle as -45 or negative 
cv2.imshow('rotated', roatated)

#Flipping an image 
flip = cv2.flip(img, -1)
cv2.imshow('flipped', flip)
# ''' 0 implies flippign the image vertically over the X-axis
# 1 implies flipping the image horizontaly over the Y-axis and 
# -1 implies to flip the image both vertically and horizontally'''


cv2.waitKey(0)