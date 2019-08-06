'''
中值滤波
让临近像素按照大小排列，取排列像素集中位于中间位置的值作为中值滤波后的像素值。
dst = cv2.medianBlur(src,ksize)
src 原图像
ksize 核大小，必须是奇数
'''
import cv2 as cv
o = cv.imread('lenanoise.png')
r = cv.medianBlur(o,3)
cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey(0)
cv.destroyAllWindows()