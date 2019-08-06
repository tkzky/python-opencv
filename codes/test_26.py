'''
laplacian算子
卷积核为
0  1  0 
1 -4  1
0  1  0

dst = cv2.lapacian(src,ddepth)

'''
import cv2 as cv
o = cv.imread('lena256.bmp')

laplacian = cv.Laplacian(o,cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian)

cv.imshow('original',o)
cv.imshow('laplacian',laplacian)
cv.waitKey()
cv.destroyAllWindows()