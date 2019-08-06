'''
图像翻转
dst = cv2.flip(src,flipCode)
flipCode < 0 上下左右翻转
flipCode = 0 上下翻转
flipCode > 0 左右翻转
'''
import cv2 as cv
a = cv.imread('lenacolor.png')
b = cv.flip(a,0)
c = cv.flip(a,1)
d = cv.flip(a,-1)
cv.imshow('a',a)
cv.imshow('b',b)
cv.imshow('c',c)
cv.imshow('d',d)
cv.waitKey(0)
cv.destroyAllWindows()