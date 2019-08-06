'''
直方图均衡化
dst = cv2.equalizeHist(src)
dst 目标图像
src 原始图像
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
o = cv.imread('hist.bmp',cv.IMREAD_GRAYSCALE)
r = cv.equalizeHist(o)
histo = cv.calcHist([o],[0],None,[256],[0,255])
histr = cv.calcHist([o],[0],None,[256],[0,255])
cv.imshow('original',o)
cv.imshow('result',r)
plt.hist(o.ravel(),256)     #绘制直方图
plt.figure()
plt.hist(r.ravel(),256)
plt.show()
cv.waitKey()
cv.destroyAllWindows()