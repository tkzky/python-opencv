'''
类型转换
cv2.cvtColor
'''
import cv2 as cv
a = cv.imread('lenacolor.png')
b = cv.cvtColor(a,cv.COLOR_BGR2GRAY)
c = cv.cvtColor(a,cv.COLOR_BGR2RGB)
cv.imshow('original',a)
cv.imshow('gray',b)
cv.imshow('rgb',c)
cv.waitKey(0)
cv.destroyAllWindows()