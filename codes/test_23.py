'''
sobel算子梯度计算
dst = cv2.Sobel(src,ddepth,dx,dy,[ksize])
dst 计算结果
src 原始图像
ddepth 处理结果图像深度 一般为-1，让处理结果与原始图像保持一致
dx x轴方向 计算x方向的梯度，dx=1,dy=0
dy y轴方向 计算y方向的梯度，dx=0,dy=1
ksize 核大小 默认为3

卷积核
-1  0  1        -1  -2  -1
-2  0  2         0   0   0
-1  0  1         1   2   1

将图像转回uint8
dst = cv2.convertScaleAbs(src)

计算两个图像的权重和
dst = cv2.addWeithted(src1,alpha,src2,beta,gamma)
dst = src1*alpha + src2*beta + gamma
'''
import cv2 as cv
import numpy as np
o =cv.imread('sobel4.bmp',cv.IMREAD_GRAYSCALE)

sobelx = cv.Sobel(o,cv.CV_64F,1,0)  #cv2.CV_64F 为了扩展像素值的取值范围
sobelx = cv.convertScaleAbs(sobelx)
sobely = cv.Sobel(o,cv.CV_64F,0,1)
sobely = cv.convertScaleAbs(sobely)
sobelxy = cv.addWeighted(sobelx,0.5,sobely,0.5,0)   #分别计算x,y方向梯度，再相加

sobelxy11 = cv.Sobel(o,cv.CV_64F,1,1)   #dx=1,dy=1，计算结果并不理想
sobelxy11 = cv.convertScaleAbs(sobelxy11)

cv.imshow('original',o)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('sobelxy',sobelxy)
cv.imshow('sobelxy11',sobelxy11)
cv.waitKey(0)
cv.destroyAllWindows()