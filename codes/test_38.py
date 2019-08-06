'''
matplotlib 中的imshow
imshow(X,cmap=None)
X       要绘制的图像
cmap    colormap,颜色图谱，默认为RGB颜色空间
        灰度图像，则 cmap = plt.cm.gray
        彩色图像，如果使用opencv读入进来的图像，默认为BGR,需要调整为RGB
'''
import cv2 as cv
import matplotlib.pyplot as plt

#灰度图像显示
o = cv.imread('girl.bmp')
r = cv.cvtColor(o,cv.COLOR_BGR2GRAY)
plt.subplot(221)
plt.imshow(o)
plt.axis('off')
plt.subplot(222)
plt.imshow(o,cmap = plt.cm.gray)
plt.axis('off')
plt.subplot(223)
plt.imshow(r)
plt.axis('off')
plt.subplot(224)
plt.imshow(r, cmap = plt.cm.gray)
plt.axis('off')
plt.show()

#彩色图像显示
b,g,r = cv.split(o)
o2 = cv.merge([r,g,b])
plt.subplot(121)
plt.imshow(o)
plt.axis('off')
plt.subplot(122)
plt.imshow(o2)
plt.axis('off')
plt.show()