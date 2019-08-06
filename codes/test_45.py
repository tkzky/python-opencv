'''
低通滤波器

'''
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
o = cv.imread('lena256.bmp',0)
dft = cv.dft(np.float32(o),flags=cv.DFT_COMPLEX_OUTPUT)
dshift = np.fft.fftshift(dft)

#构建低通滤波器
rows,cols = o.shape
crow,ccol = int(rows/2),int(cols/2)
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30] = 1

fshift = dshift * mask
ishift = np.fft.ifftshift(fshift)
io = cv.idft(ishift)
io = cv.magnitude(io[:,:,0],io[:,:,1])

plt.subplot(121)
plt.imshow(o,cmap='gray')
plt.axis('off')
plt.title('original')
plt.subplot(122)
plt.imshow(io,cmap='gray')
plt.axis('off')
plt.title('result')
plt.show()
