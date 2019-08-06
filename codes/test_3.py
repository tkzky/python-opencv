'''
    使用numpy访问像素
    主要使用函数image.item(位置参数)访问像素
    使用image.itemset(位置参数，新值)更改像素值
'''
import cv2 as cv
import numpy as np
i = cv.imread('lena.png',cv.IMREAD_UNCHANGED)
print(i.item(100,100,0))
i.itemset((100,100,0),255)
print(i.item(100,100,0))

print(i.item(100,100,1))
i.itemset((100,100,1),255)
print(i.item(100,100,1))