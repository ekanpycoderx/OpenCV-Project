import cv2
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
#500 = height, 500 = width , 3 = non. of channels

cv2.imshow('Blank', blank)

#PAINTING/ DRAWING AN IMAGE
# 1. Paint the image a certain color
blank[:] = 255,0,0 # This shows us the blue color we can also change it to 0,0,255 for red color and 0,255,0 for green color
cv2.imshow('Blue', blank)
#We can also call a certain portion of the image formed by basically giving it the number of pixels/ range
blank[200:300, 300:400] = 0,255,0 # This shows us the green color
cv2.imshow('Green', blank) 
#Note that the background of the previous image  formed has been taken into account

# 2. Draw a Rectangle
cv2.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = 2) #We can also writhe the thickness as cv.FILLED to fill in the rectangle we are drawing in here
cv2.imshow('Rectangle', blank)
cv2.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = cv2.FILLED) #We can also write -1 instead of writing the whole thing again 
cv2.imshow('Rectangle', blank)

#We can also re-write this as 
cv2.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness = cv2.FILLED) #We can also specify this as -1 instead of writing the whole thing
cv2.imshow('Rectangle', blank)
#Remember the fact that 1 stands for width and 0 stands for height and we divide the original image dimensions by 2

# 3. Draw a circle
cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 250, (0,0,255), thickness = 3)
#Here 250 is the specifyign the radius of the circle by giving it the number of pixels so here the radius of our circle is 250 pixels in lenght
cv2.imshow('Circle and Rectangle', blank)

# 4. Draw a line
cv2.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
#0,0 is the starting point and then (blank.shape[1]//2, blank.shape[0]//2) is the ending point and 255,255,255 is the color of the line here it is for the white color
cv2.imshow('Line', blank)

# 5. Writing text on a image
cv2.putText(blank, 'Hi there', (225,225), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv2.imshow('Text', blank)
#HERE (225,225) is the point from where we will start writing the text
#opencv comes with many types of fonts so we are using the given font here
#1.0 is the size of the text mentioned here
# 2 is the thickness of the ink or of the letter we are using in theer
#255,255,255 is the color of the text displayed on the screen


#img = cv2.imread('assets/pic.jpg')

#cv2.imshow('Image', img)

cv2.waitKey(0)