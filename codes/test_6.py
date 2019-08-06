'''
通道的拆分与合并
1 拆分通道 split(img) 
2 合并通道 merge([b,g,r])
'''
import cv2 as cv
a = cv.imread('lenacolor.png')
b,g,r = cv.split(a)
cv.imshow('original',a)
cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

m = cv.merge([b,g,r])
cv.imshow('result',m)

n=cv.merge([r,g,b])
cv.imshow('result_2',n)

cv.waitKey(0)
cv.destroyAllWindows()