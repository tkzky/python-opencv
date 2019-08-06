'''
subplot函数
subplot(nrows,ncols,plot_number)
nrows       行数
ncols       列数
plot_number 窗口序号
'''
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('boat.bmp',cv.IMREAD_GRAYSCALE)
equ = cv.equalizeHist(img)
plt.subplot(121),plt.hist(img.ravel(),256)
plt.subplot(122),plt.hist(equ.ravel(),256)
plt.show()