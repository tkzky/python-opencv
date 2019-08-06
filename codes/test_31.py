'''
图像轮廓
轮廓是什么？
—边缘检测能够检测出边缘，但边缘是不连续的
—将边缘连接成一个整体，构成轮廓
注意：
1、对象是二值图像，所以需要预先进行阈值分割或者边缘检测处理
2、查找轮廓需要更改原始图像，因此通常使用原始图像的一份拷贝图像操作
3、在opencv中，是从黑色背景中查找白色对象。因此对象必须是白色的，背景必须是黑色的。

--------------------------------------------------------------------------------------------
cv2.findContours()  查找图像轮廓
cv2.drawContours()  将查找到的轮廓绘制到图像上

--------------------------------------------------------------------------------------------
contours,hierarchy = cv2.findContours(image,mode,method)
                                        image 原始图像
contours 轮廓                           mode 轮廓检索模式
hierarchy 图像的拓扑信息（轮廓层次）     method 轮廓的近似方法

mode 轮廓检索模式
cv2.RETR_EXTERNAL   表示只检测外轮廓
cv2.RETR_LIST       检测的轮廓不建立等级关系
cv2.RETR_CCOMP      建立两个等级的轮廓，上面的一层为外边界，里面的一层为内孔的边界信息。
                    如果内孔内还有一个连通物体，这个物体的边界也在顶层。
cv2.RETR_TREE       建立一个等级树结构的轮廓

method 轮廓的近似方法
cv2.CHAIN_APPROX_NONE       存储所有轮廓点，相邻的两个点的像素位置差不超过1
                            即max(abs(x1-x2),abs(y2-y1)) == 1
cv2.CHAIN_APPROX_SIMPLE     压缩水平方向，垂直方向，对角线方向的元素
                            只保留该方向的终点坐标，例如一个矩形轮廓只需要4个点来保存轮廓信息
cv2.CHAIN_APPROX_TC89_L1    使用teh-Chinl chain 近似算法
cv2.CHAIN_APPROX_TC89_KCOS  使用teh-Chinl chain 近似算法

-------------------------------------------------------------------------------------------------
r = cv2.drawContours(o,contours,contourldx,color[,thickness])
r               目标图像，直接修改目标的像素数，实现绘制
o               原始图像
contours        需要绘制的边缘数组
contourldx      需要绘制的边缘索引，如果全部绘制则为-1
color           绘制的颜色，为BGR格式的Scalar (B,G,R)
thickness       可选，绘制的密度，即描绘轮廓时所用的画笔的粗细
'''

import cv2 as cv
o = cv.imread('contours.bmp')
gray = cv.cvtColor(o,cv.COLOR_BGR2GRAY)                     #类型转换，转换成灰度图像
ret,binary = cv.threshold(gray,127,255,cv.THRESH_BINARY)    #二进制阈值分割
contours,hierarchy = cv.findContours(binary,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
co = o.copy()
r = cv.drawContours(co,contours,-1,(255,0,0),3)

cv.imshow('original',o)
cv.imshow('result',r)
cv.waitKey()
cv.destroyAllWindows()