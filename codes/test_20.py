'''
图像梯度
膨胀图像-腐蚀图像  得到轮廓信息
梯度(img) = 膨胀(img) - 腐蚀(img)
result = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
'''
import cv2 as cv
import numpy as np
o = cv.imread('gradient.png')
k = np.ones((5,5),np.uint8)
r = cv.morphologyEx(o,cv.MORPH_GRADIENT,k)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()