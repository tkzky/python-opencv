'''
掩膜图像生成
cv2.bitwise_and(image,mask)
'''
import cv2 as cv
import numpy as np
o = cv.imread('boat.bmp')
m = np.zeros(o.shape,np.uint8)
m [300:500,300:500] = 255
mi = cv.bitwise_and(o,m)
cv.imshow('original',o)
cv.imshow('mask',m)
cv.imshow('result',mi)
cv.waitKey()
cv.destroyAllWindows()