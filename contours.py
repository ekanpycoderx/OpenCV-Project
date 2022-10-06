import cv2
import numpy as np

img = cv2.imread('assets/pic.jpg')

# Use Ctrl + / for commenting multiple lines

#Countours are basically the boundaries of objects, the line or curve that joins the 
#continuous points along the boundary of an object. Note that they are not exactly the same as edges mathematically but look the same as edges

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('Blank', blank)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

# blur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
# cv2.imshow('blur', blur)

canny = cv2.Canny(img, 125, 175)
cv2.imshow('Canny Edges', canny)

ret , thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY) # for now the threshold function just looks at an image and tries to binarise it 
# So if the density of a pixel is below 125 it's going to be set to 0 for black
# and if it is above 125 then it is set to 255 of white
#125 is the threshold value and 255 is the maximum threshold value
cv2.imshow('Thresh', thresh)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#  here we can wrtie RETR_TREE if we want all herarchial contours or
# 1. RETR_EXTERNAL for only the external contours or all the ones on the outsidde
# 2. RETR_LIST shows all the contours found in the given image
# 3. CHAIN_APPROX_is a contour approximation method this is basically how we want to approximate the contour
# 4. CHAIN_APPROX_NONE returns nothign sometimes people also use
# 5. CHAIN_APPROX_SIMPLE which essentially compresses all the contours that are returned in the ismple one that make most sense
# 6. for eg if we have a line in an image if we use CHAIN_APPROX_NONE we get all the contours all the coordinate 
# of the points of that line where as CHAIN_APPROX_SIMPLE essentially takes all of the point of the line and then defines the line by it's 2 end points
# 7. contours here is a list of co ordinates of all the contours found in this image

print(f'{len(contours)} contour(s) found!!')

# This example below shows how we are transposing and drawing by joining all the contours again 
# which opencv found out for us in the previous part 
# so first we got a blank image then we used the drawcontours method to superimpose our image on
# the blank image where -1 stands for drawing all the contours and 0,255,0 stands for green color
# and the 1 stands for the thickness of the ink/ pen.  

cv2.drawContours(blank, contours, -1, (0,255,0), 1)
cv2.imshow('Contours drawn', blank)

cv2.waitKey(0)
