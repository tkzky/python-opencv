'''
canny边缘检测
过程： 去噪、梯度、非极大值抑制、泄后阈值
edges = cv.Canny(img,threshold1,threshold2)
threshold1 minVal阈值1
threshold2 maxVal阈值2
阈值越小，边界越丰富
'''
import cv2 as cv
o = cv.imread('lena256.bmp',cv.IMREAD_GRAYSCALE)
r1 = cv.Canny(o,100,200)
r2 = cv.Canny(o,64,128)

cv.imshow('original',o)
cv.imshow('canny1',r1)
cv.imshow('canny2',r2)
cv.waitKey()
cv.destroyAllWindows()