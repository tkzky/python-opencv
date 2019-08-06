'''
直方图
直方图横坐标为图像中各个像素点的灰度级，纵坐标为具有该灰度级的像素个数
归一化直方图横坐标为图像中各个像素点的灰度级，纵坐标为出现这个灰度级的概率

hist(数据源，像素级)
数据源：图像，必须是一维数组
像素级：一般是256，指[0,255]

ravel
将多维数组降为一维数组
一维数组 = 多维数组.ravel()
'''
import cv2 as cv
import matplotlib.pyplot as plt
o = cv.imread('boat.bmp')
cv.imshow('original',o)
plt.hist(o.ravel(),256)
plt.show()
cv.waitKey()
cv.destroyAllWindows()
