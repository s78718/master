#coding=utf-8
import cv2
import numpy as np
 
img = cv2.imread("C:\\Users\\s7871\\Pictures\\6.png",cv2.IMREAD_GRAYSCALE)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
x = cv2.Sobel(img,cv2.CV_16S,2,0)
y = cv2.Sobel(img,cv2.CV_16S,0,2)
 
absX = cv2.convertScaleAbs(x)
absX=cv2.flip(absX,-1)
absY = cv2.convertScaleAbs(y)
 
dst = cv2.addWeighted(absX,2,absY,2,0)
 
cv2.imshow("absX", absX)
cv2.imshow("absY", absY)
cv2.imshow("Result", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
