'''
开运算
开运算(image) = 膨胀(腐蚀(image))
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
opening 开运算结果
img 原图像
cv2.MORPH_OPEN 开运算
kernel 卷积核
'''
import cv2 as cv
import numpy as np
o = cv.imread('erode.png')
k = np.ones((10,10),np.uint8)
r = cv.morphologyEx(o,cv.MORPH_OPEN,k)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()