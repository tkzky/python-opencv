import cv2
i = cv2.imread('lena.png')
cv2.imshow('original',i)
i[200:230,200:230] = [255,255,255]
cv2.imshow('result',i)
cv2.waitKey(0)
cv2.destroyAllWindows()