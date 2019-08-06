'''
图像平滑
均值滤波
处理结果 = cv2.blur(原始图像，核大小)
核大小：以(宽度，高度)形式表示的元组
'''
import cv2 as cv
o = cv.imread('lenanoise.png')
b = cv.blur(o,(5,5))
cv.imshow('original',o)
cv.imshow('result',b)
cv.waitKey(0)
cv.destroyAllWindows()