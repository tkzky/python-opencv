'''
numpy实现傅里叶变换
numpy.fft.fft2      实现傅里叶变换，返回一个复数数组(complex ndarray)
numpy.fft.fftshift  将零频率分量移到频谱中心
20*np.log(np.abs(fshift))   设置频谱范围
注意：
1、傅里叶得到低频、高频信息，针对低频、高频处理能够实现不同的目的
2、傅里叶过程是可逆的，图像经过傅里叶变换、逆傅里叶变换后能够恢复原来的图像
3、在频域对图像进行处理，在频域的处理会反映在逆变换图像上
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
o = cv.imread('lena256.bmp',0)
f = np.fft.fft2(o)
fshift = np.fft.fftshift(f)
result = 20*np.log(np.abs(fshift))
plt.subplot(121)
plt.imshow(o,cmap=plt.cm.gray)
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(result,cmap=plt.cm.gray)
plt.title('result')
plt.axis('off')
plt.show()