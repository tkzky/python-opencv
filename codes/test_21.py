'''
图像礼帽
礼帽图像 = 原始图像 - 开运算图像
得到噪声图像
礼帽(img) = img - 开运算(img)
result = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
'''
import cv2 as cv
import numpy as np
o = cv.imread('tophat.png')
k = np.ones((5,5),np.uint8)
r = cv.morphologyEx(o,cv.MORPH_TOPHAT,k)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()