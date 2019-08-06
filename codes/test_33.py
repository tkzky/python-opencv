'''
利用opencv统计直方图
calcHist
hist = cv2.calcHist(images,channels,mask,histSize,ranges,accumulate)
hist        直方图，是一个二维数组
images      原始图像,用[]括起来
channels    指定通道，输入图像是灰度图时，它的值为[0]；彩色图像时可以是[0],[1],[2]分别对应BGR
mask        掩码图像，只统计图像某一部分的直方图，需要掩码图像；不需要则用None
histSize    BINS的数量，一般[256]
ranges      像素值范围RANGE，一般[0,255]
accumulate  累计标识，默认为false；对于一组图像的直方图统计，用true

'''
import cv2 as cv
import matplotlib.pyplot as plt

o = cv.imread('boat.bmp')
hist = cv.calcHist([o],[0],None,[256],[0,255])
print(type(hist))
print(hist.size)
print(hist.shape)
cv.imshow('original',o)
plt.plot(hist,color='r')
plt.show()

g = cv.imread('girl.bmp')
histb = cv.calcHist([g],[0],None,[256],[0,255])
histg = cv.calcHist([g],[1],None,[256],[0,255])
histr = cv.calcHist([g],[2],None,[256],[0,255])
cv.imshow('girl',g)
plt.plot(histb,color = 'b')
plt.plot(histg,color = 'g')
plt.plot(histr,color = 'r')
plt.show()
cv.waitKey()
cv.destroyAllWindows()