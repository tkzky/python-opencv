'''
高通滤波
低频对应于图像内变化缓慢的灰度分量
高频对应于图像内变化越来越快的灰度分量，是由灰度的尖锐过渡造成的
频域滤波：
    修改傅里叶变换以达到某种目的，然后计算IDFT返回到图像域
    特殊目的：图像增强、图像去噪、边缘检测、特征提取、压缩、加密等
低通滤波器：衰减高频而通过低频，将模糊一幅图像
高通滤波器：衰减低频而通过高频，将增强尖锐的细节，但是会导致图像对比度降低
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
o = cv.imread('lena256.bmp',0)
f = np.fft.fft2(o)
fshift = np.fft.fftshift(f)

#构建高通滤波器
rows,cols = o.shape
crows,ccols = int(rows/2),int(cols/2)
fshift[crows-30:crows+30,ccols-30:ccols+30] = 0

ishift = np.fft.ifftshift(fshift)
io = np.fft.ifft2(ishift)
io = np.abs(io)
plt.subplot(121)
plt.imshow(o,cmap=plt.cm.gray)
plt.axis('off')
plt.title('orriginal')
plt.subplot(122)
plt.imshow(io,cmap=plt.cm.gray)
plt.title('result')
plt.axis('off')
plt.show()

