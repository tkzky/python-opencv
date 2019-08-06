'''
方框滤波
处理结果 = cv2.boxFilter(原始图像，目标图像深度，核大小，normalize属性)
目标图像深度：int 类型的目标图像深度。通常使用“-1”表示与原图像一致。
normalize属性：是否对目标图像进行归一化处理。 
    true(normalize=1)或省略:与均值滤波相同  false(normalize=0):相加不平均，不进行归一化处理,很容易发生溢出
'''
import cv2 as cv
o = cv.imread('lenanoise.png')
r = cv.boxFilter(o,-1,(5,5))    #默认，就是归一化处理，为均值滤波
r2 = cv.boxFilter(o,-1,(5,5),normalize=0)   #不进行归一化处理
r3 = cv.boxFilter(o,-1,(2,2),normalize=0)   #不进行归一化处理
cv.imshow('original',o)
cv.imshow('result1',r)
cv.imshow('result2',r2)
cv.imshow('result3',r3)
cv.waitKey()
cv.destroyAllWindows()