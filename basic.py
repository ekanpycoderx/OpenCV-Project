import cv2

img = cv2.imread('assets/pic.jpg')

cv2.imshow('image', img)

# 1. COnverting an image to grayscale
#Note that the wokring of pixels in opcv is based on BGR that is Blue,Green,Red
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# 2. Blurring an image
#Here we are using the Gaussian Blur
blur = cv2.GaussianBlur(img, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow('blur', blur)

# 3. Edge cascade
canny = cv2.Canny(img , 125, 175)
cv2.imshow('Canny edges' , canny)
#Basically it detects the edges present in an image 
#We can also reduce the number of edges found by applying a lot of blur or remove some of the edges by blurring it a bit

# 4. Dilating the image
dilated = cv2.dilate(canny, (3,3), iterations=6) #Iterations make the image more dialted and thickens the image edges
cv2.imshow('Dialated', dilated)

# 5. Eroding an image
eroded = cv2.erode(canny, (3,3), iterations=6)
cv2.imshow('Eroded', eroded)
#Basically eroded function removes the changes done by dialated and redo them 
#This change can be comapred from the image producaed from the function of edge cascade
#They almost look the same in the size and shape including the thicknes of edges
#Note that the iternations should also be same to completly remove the affect done by dialated image 

# 6. Resizing and cropping an image 
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA) 
#(500,500) means the new dimensions of the new image formed
#interpolation helps in resizing the image to a smaller dimension than the original image given
#For enlarging the image we may use INTER_LINEAR or INTER_CUBIC
cv2.imshow('resized', resized)

# 7. Cropping the image 
cropped = img[50:500, 500:900] #Selecting the no. of pixels/ range of pixels
cv2.imshow('cropped', cropped)

cv2.waitKey(0)