'''
向上取样
图像放大
dst = cv2.pyrUp(src)
'''
import cv2 as cv
o = cv.imread('lena256.bmp',cv.IMREAD_GRAYSCALE)
r1 = cv.pyrUp(o)
r2 = cv.pyrUp(r1)

cv.imshow('original',o)
cv.imshow('pyrUp1',r1)
cv.imshow('pyrUp2',r2)
cv.waitKey()
cv.destroyAllWindows()