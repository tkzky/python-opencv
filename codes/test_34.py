'''
掩膜直方图

'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

o = cv.imread('boat.bmp',cv.IMREAD_GRAYSCALE)
m = np.zeros(o.shape,np.uint8)
m[200:400,200:400] = 255
histo = cv.calcHist([o],[0],None,[256],[0,255])
histm = cv.calcHist([o],[0],m,[256],[0,255])
plt.plot(histo)
plt.plot(histm)
plt.show()