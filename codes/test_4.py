'''
获取图像属性
1 形状 shape 可以获取图像的形状，返回包括行数，列数，通道数的元组
2 像素数目 size 可以获得图像像素数目，灰度图像返回 行数*列数；彩色图像返回 行数*列数*通道数
3 图像类型 dtype 返回图像每一个像素点的数据类型 unit8
'''

import cv2 as cv
a = cv.imread('lenacolor.png',cv.IMREAD_UNCHANGED)
print(a.shape)
print(a.size)
print(a.dtype)