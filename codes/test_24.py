'''
scharr算子
使用3*3 sobel算子可能不太精准，scharr算子效果会更好。
与sobel算子计算速度相同，不同的只是系数不同
是sobel算子的改进
dst = cv2.Scharr(src,ddepth,dx,dy)
满足条件: dx>=0 && dy>=0 && dx+dy==1
    一般 dst = cv2.Scharr(src,cv2.CV_64F,dx,dy)
         dst = cv2.convertScaleAbs(dst)
等价于
dst = cv2.Sobel(src,ddpeth,dx,dy,-1)    #改进sobel算子

卷积核
-3  0  3        -3  -10  -3
-10 0 10         0   0   0
-3  0  3         3  10   3
'''
import cv2 as cv
import numpy as np
o = cv.imread('scharr.bmp')

scharrx = cv.Scharr(o,cv.CV_64F,1,0)
scharrx = cv.convertScaleAbs(scharrx)
scharry = cv.Scharr(o,cv.CV_64F,0,1)
scharry = cv.convertScaleAbs(scharry)
scharrxy = cv.addWeighted(scharrx,0.5,scharry,0.5,0)

cv.imshow('original',o)
cv.imshow('scharr',scharrxy)
cv.waitKey()
cv.destroyAllWindows()

