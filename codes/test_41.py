'''
numpy 实现傅里叶逆变换
傅里叶过程是可逆的，图像经过傅里叶变换、逆傅里叶变换后能够恢复原来的图像
在频域对图像进行处理，在频域的处理会反映在逆变换图像上
numpy.fft.ifft2      实现傅里叶逆变换，返回一个复数数组(complex ndarray)
numpy.fft.ifftshift  将零频率分量移到频谱中心
iimg = np.abs(逆傅里叶变换的结果)
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
o = cv.imread('boat.bmp',0)
f = np.fft.fft2(o)
fshift = np.fft.fftshift(f)
ishift = np.fft.ifftshift(fshift)
io = np.fft.ifft2(ishift)
io = np.abs(io)
plt.subplot(121)
plt.imshow(o,cmap=plt.cm.gray)
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(io,cmap=plt.cm.gray)
plt.title('result')
plt.axis('off')
plt.show()