'''
sobel和scharr算子比较
'''
import cv2 as cv
o = cv.imread('lena256.bmp',cv.IMREAD_GRAYSCALE)

sobelx = cv.Sobel(o,cv.CV_64F,1,0)
sobelx = cv.convertScaleAbs(sobelx)
sobely = cv.Sobel(o,cv.CV_64F,0,1)
sobely = cv.convertScaleAbs(sobely)
sobelxy = cv.addWeighted(sobelx,0.5,sobely,0.5,0)

scharrx = cv.Scharr(o,cv.CV_64F,1,0)
scharrx = cv.convertScaleAbs(scharrx)
scharry = cv.Scharr(o,cv.CV_64F,0,1)
scharry = cv.convertScaleAbs(scharry)
scharrxy = cv.addWeighted(scharrx,0.5,scharry,0.5,0)

cv.imshow('original',o)
cv.imshow('sobel',sobelxy)
cv.imshow('scharr',scharrxy)
cv.waitKey()
cv.destroyAllWindows()