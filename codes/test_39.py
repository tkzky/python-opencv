'''
直方图均衡化对比
'''
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('hist.bmp',cv.IMREAD_GRAYSCALE)
equ = cv.equalizeHist(img)
plt.subplot(221)
plt.imshow(img,cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(222)
plt.imshow(equ,cmap=plt.cm.gray)
plt.axis('off')
plt.subplot(223)
plt.hist(img.ravel(),256)
plt.subplot(224)
plt.hist(equ.ravel(),256)
plt.show()