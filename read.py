import cv2 
#importing cv2 libraray

img = cv2.imread('assets/pic.jpg')
#we are assigning an image named img by reading the image using the cv2.imread function and tellling it the directory here assests/pic.jpg that where the image is located

cv2.imshow('Windows', img)
#This function shows us the image and 'Window' is the name of the frame and the image is img shown here

cv2.waitKey(0)
''' Waits for a key to be entered to exit/terminate by the time'''