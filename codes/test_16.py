'''
图像腐蚀
腐蚀针对的是二值图像
dst = cv2.erode(src,kernel,iterations)
dst 处理结果
src 原图像
kernal 卷积核
iterations 迭代次数,默认是1
'''
import cv2 as cv
import numpy as np
o = cv.imread('erode.png')
k = np.ones((5,5),np.uint8)
r = cv.erode(o,k,iterations=2)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()