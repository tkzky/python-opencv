'''
拉普拉斯金字塔
Li = Gi - pyrUp(pyrDown(Gi))
Gi 原始图像
Li 第i层拉普拉斯金字塔图像
'''
import cv2 as cv
o = cv.imread('lena256.bmp',cv.IMREAD_GRAYSCALE)

#第0层拉普拉斯金字塔图像
od = cv.pyrDown(o)
odu = cv.pyrUp(od)
lappyr0 = o - odu

#第1层拉普拉斯金字塔图像
o1 = od
od1 = cv.pyrDown(o1)
od1u = cv.pyrUp(od1)
lappyr1 = o1 - od1u

cv.imshow('original',o)
cv.imshow('lappyr0',lappyr0)
cv.imshow('lappyr1',lappyr1)

cv.waitKey()
cv.destroyAllWindows()
