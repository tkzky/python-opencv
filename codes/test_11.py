'''
阈值分割
threshold函数
retval,dst = cv2.threshold(src,thresh,maxval,type)
retval 阈值   dst 处理结果
src 原图像, thresh 阈值, maxval 最大值, type 类型
    二进制阈值化 cv2.THRESH_BINARY
    反二进制阈值化 cv2.THRESH_BINARY_INV
    截断阈值化 cv2.THRESH_TRUNC
    反阈值化为零 cv2.THRESH_TOZERO_INV
    阈值化为零 cv2.THRESH_TOZERO
'''
import cv2 as cv
o = cv.imread('lena256.bmp',cv.IMREAD_UNCHANGED)
r,b = cv.threshold(o,128,255,cv.THRESH_BINARY)          #二进制阈值化
r2,b2 = cv.threshold(o,128,255,cv.THRESH_BINARY_INV)    #反二进制阈值化
r3,b3 = cv.threshold(o,128,255,cv.THRESH_TRUNC)         #截断阈值化
r4,b4 = cv.threshold(o,128,255,cv.THRESH_TOZERO_INV)    #反阈值化为零
r5,b5 = cv.threshold(o,128,255,cv.THRESH_TOZERO)        #阈值化为零
cv.imshow('original',o)
cv.imshow('result',b)
cv.imshow('result2',b2)
cv.imshow('result3',b3)
cv.imshow('result4',b4)
cv.imshow('result5',b5)
cv.waitKey(0)
cv.destroyAllWindows()