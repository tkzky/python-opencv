'''
图像膨胀
是腐蚀的逆操作，用于去噪
图像被腐蚀后，去除了噪声但是会压缩图像
对腐蚀后的图像进行膨胀，可以去除噪声，并保持原有的形状
先腐蚀后膨胀称为开运算
dst = cv2.dilate(src,kernel,iterations)
dst 处理结果
src 原图像
kernel 卷积核
iterations 迭代次数
'''
import cv2 as cv
import numpy as np
o = cv.imread('dilate.png')
k = np.ones((5,5),np.uint8)
r = cv.dilate(o,k,iterations=2)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()