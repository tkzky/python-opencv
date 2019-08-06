'''
向下取样
图像缩小
dst = cv2.pyrDown(src)
'''
import cv2 as cv
o = cv.imread('lena256.bmp',cv.IMREAD_GRAYSCALE)
r1 = cv.pyrDown(o)
r2 = cv.pyrDown(r1)

cv.imshow('original',o)
cv.imshow('pyrDown1',r1)
cv.imshow('pyrDown2',r2)
cv.waitKey()
cv.destroyAllWindows()