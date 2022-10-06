import cv2
import numpy as np


img = cv2.imread('assets/pic.jpg')

blank = np.zeros(img.shape[:2], dtype='uint8')
#We create a blank image on which we transpose the arrays we want to check what part
#is the the given color is making of the image

b,g,r = cv2.split(img) #Split funtion splits the given image into the components of BGR

blue = cv2.merge([b,blank,blank])#Blue, Green, Red
green = cv2.merge([blank,g,blank])#Blue, Green, Red
red = cv2.merge([blank,blank,r])#Blue, Green, Red
# all = cv2.merge([b,g,r])#Blue, Green, Red
# cv2.imshow('all', all)
bg = cv2.merge([b,g,blank])
rg = cv2.merge([blank,g,r])
cv2.imshow('rg', rg)
cv2.imshow('bg', bg)
cv2.imshow('blue', blue)
cv2.imshow('green',green)
cv2.imshow('red',red)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

merged = cv2.merge([b,g,r])
cv2.imshow('merged', merged)#Another way of merging all of them
cv2.waitKey(0)