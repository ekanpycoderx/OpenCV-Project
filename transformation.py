import cv2
import numpy as np
import sys

img = cv2.imread('assets/pic.jpg')

# 1. Translation 
#Basically shifting an image along the X and Y axis so using translation we can shift the image up down left or right
def translate(img, x, y):
    #x stands for no. of pixels i want to shift along x and y stands for no. of pixels i want to shift along y axis
    transmat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transmat, dimensions)

# -x --> left
# -y --> Up
# x ---> Right
# y --> Down

def asker():
    x_input = input('Enter the pixels count to move on X-axis : ')
    y_input = input('Enter the pixels count to move on Y-axis : ')
    translated = translate(img, x_input, y_input)
    cv2.imshow('translated', translated)
    cv2.waitKey(5)
    asker()

asker()