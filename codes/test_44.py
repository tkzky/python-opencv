'''
opencv 实现逆傅里叶变换

返回结果 = cv2.idft(原始数据)
返回结果：取决于原始数据的类型和大小
原始数据：实数和复数均可

返回值 = cv2.magnitude(参数1，参数2)
计算幅值

'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
o = cv.imread('lena256.bmp',0)
dft = cv.dft(np.float32(o),flags=cv.DFT_COMPLEX_OUTPUT)
fshift = np.fft.fftshift(dft)
ifshift = np.fft.ifftshift(fshift)
io = cv.idft(ifshift)
io = cv.magnitude(io[:,:,0],io[:,:,1])
plt.subplot(121)
plt.imshow(o,cmap='gray')
plt.title('original')
plt.axis('off')
plt.subplot(122)
plt.imshow(io,cmap='gray')
plt.axis('off')
plt.title('result')
plt.show()