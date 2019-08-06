'''
高斯滤波
让临近的像素具有更高的重要程度，对周围像素计算加权平均值，较近的像素具有较大的权重值
dst = cv2.GaussianBlur(src,ksize,sigmaX)
src: 原图像
ksize: 核大小
sigmaX: X方向方差，控制权重。sigmaX=0时：sigmaX=0.3*((ksize-1)*0.5-1)+0.8
'''
import cv2 as cv
o = cv.imread('lenanoise.png')
r = cv.GaussianBlur(o,(5,5),0)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()