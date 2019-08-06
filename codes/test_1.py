import cv2
src = cv2.imread('Demo.png')
cv2.imshow('Demo',src)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Demo2.png',src)