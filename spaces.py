import cv2
import matplotlib.pyplot as plt

#Btw use Ctrl + U to uncomment whatever number of lines you want to

img = cv2.imread('assets/pic.jpg')

# Color spaces -- A system of representing an array of pixels 
# for example RGB is a Color space and grayscale is also a type of Color space

#BGR is opencv's default way of reading images
#BGR to Grayscale conversion
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale', gray)
# For reversing just change COLOR_BGR2GRAY to COLOR_GRAY2BGR
# Note that we can't directly convert grayscale to hsv

#BGR to HSV conversion
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)
# We can do the reverse also by changing COLOR_BGR2HSV to COLOR_HSV2BGR

#BGR to L-A-B
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('lab', lab)
# COLOR_BGR2LAB --> COLOR_LAB2BGR for reversing the changes

cv2.imshow('image', img)

#BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb', rgb)#We gave opencv and rgb image but it assumed it was an BGR image SUS
plt.imshow(rgb)
plt.show() #We can also check matplotlib to check whatthe image looks like in RGB because opencv is unable ot show this image in the BGR format as in the result

cv2.waitKey(0)

# This shows what a BGR image generally looks like without a library like opencv to handle it
# Because matplotlib doesn't know that the image is in BGR so itdisplays it as an RGB 
# this was we can see the inversion happening at this place
# plt.imshow(img)
# plt.show()