import cv2
import numpy as np


img = cv2.imread('assets/pic.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

#Laplation
lap = cv2.Laplacian(gray, cv2.CV_64F) #Here CV_64F is the D depth
lap = np.uint8(np.absolute(lap)) #np.absolute() converts all the negative pixel values to their absolute value that is |x| bc pixels can't be -ve
cv2.imshow('lap',lap)

#Sobel
#Sobel computes the gradients in 2 directions x and y
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0) #X direction is 1
sobely = cv2.Sobel(gray,cv2.CV_64F, 0, 1)#Y direction is 1
combined = cv2.bitwise_or(sobelx , sobely) #bitwise operator
cv2.imshow('sobely', sobely)
cv2.imshow('sobelx', sobelx)
cv2.imshow('combined', combined)

canny = cv2.Canny(gray, 150, 175)#150 and 175 are the threshold values
cv2.imshow('Canny', canny) #Bsically shows a pencil shaded image of the grayscale
cv2.waitKey(0)