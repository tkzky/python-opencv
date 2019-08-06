'''
闭运算
先膨胀，后腐蚀
有助于关闭前景物体内部的小孔，或物体上的小黑点
闭运算(img) = 腐蚀(膨胀(img))
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
closing 闭运算结果
img 原图像
cv2.MORPH_CLOSE 闭运算
kernel 卷积核
'''
import cv2 as cv
import numpy as np
o = cv.imread('closing.png')
k = np.ones((15,15),np.uint8)
r = cv.morphologyEx(o,cv.MORPH_CLOSE,k)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()