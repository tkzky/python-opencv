'''
图像加法运算
1 numpy实现 结果 = 图像1+图像2 如果结果像素值>255,结果对255取模
2 opencv实现 cv2.add(图像1，图像2) 如果结果像素值>255，取255
'''
import cv2 as cv
import numpy as np
a = cv.imread('lena256.bmp')
b = a+a
c = cv.add(a,a)
cv.imshow('original',a)
cv.imshow('result_1',b)
cv.imshow('result_2',c)
cv.waitKey(0)
cv.destroyAllWindows()

'''
图像融合
将2张或2张以上图像相加组成新的图像
addWeighted()
dst = cv2.addWeighted(src1,alpha,src2,beta,gamma)
dst = src1*alpha+src2*beta+gamma
参数gamma不能省略
'''