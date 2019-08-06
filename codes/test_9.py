'''
图像缩放
dst=cv2.resize(src,dsize[,dst[,fx[,fy[,interpolation]]]])
src 原始图像
dsize 缩放大小  列 行
fx,fy 缩放大小  列 行
'''
import cv2 as cv
a = cv.imread('lenacolor.png')
b = cv.resize(a,(200,100))      #200列，100行
c = cv.resize(a,None,fx=0.5,fy=1)  #fx 水平方向  fy 竖直方向
cv.imshow("a",a)
cv.imshow('b',b)
cv.imshow('c',c)
cv.waitKey(0)
cv.destroyAllWindows()