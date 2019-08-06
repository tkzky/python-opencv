'''
感兴趣区域ROI（region of interest）
从被处理图像以方框、圆等方式勾勒出需要处理的部分，
可以通过各种算子和函数来求得感兴趣区域ROI并进行图像的下一步处理
'''
import cv2 as cv
import numpy as np
a = cv.imread('lenacolor.png',cv.IMREAD_UNCHANGED)
b = np.ones((101,101,3))
b = a[220:400,250:350]
cv.imshow('face',b)
cv.waitKey(0)
cv.destroyAllWindows()