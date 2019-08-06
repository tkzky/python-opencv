'''
黑帽图像运算
黑帽图像 = 闭运算图像 - 原始图像
得到图像内部的小孔，或前景中的黑点
黑帽(img) = 闭运算(img) - img
result = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
'''
import cv2 as cv
import numpy as np
o = cv.imread('blackhat.png')
k = np.ones((5,5),np.uint8)
r = cv.morphologyEx(o,cv.MORPH_BLACKHAT,k)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()