'''
opencv 实现傅里叶变换
返回结果 = cv2.dft(原始图像，转换标识)
返回结果    是双通道的，第一个通道是实数部分，第二个通道是虚数部分
原始图像    输入图像要首先换算成np.float32格式， np.floatt32(img)
转换标识    flags = cv2.DFT_COMPLEX_OUTPUT，输出一个复数矩阵

计算幅值
返回值 = cv2.magnitude(参数1，参数2)
参数1：浮点型X坐标值，也就是实部
参数2：浮点型Y坐标值，也就是虚部
'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
o = cv.imread('lena256.bmp',0)
dft = cv.dft(np.float32(o),flags=cv.DFT_COMPLEX_OUTPUT)
dshift = np.fft.fftshift(dft)
result = 20*np.log(cv.magnitude(dshift[:,:,0],dshift[:,:,1]))
plt.subplot(121)
plt.imshow(o,cmap='gray')
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(result,cmap='gray')
plt.title('result')
plt.axis('off')
plt.show()