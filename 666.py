# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 11:15:53 2019

@author: s7871
"""

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\s7871\\Pictures\\Saved Pictures\\\icon\\20180720113105873.png",1)
img = cv2.imread("C:\\Users\\s7871\\Pictures\\Saved Pictures\\\icon\\762908e014af58dd6e8119d0.png",1)

img1=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img1=cv2.medianBlur(img1,3) 


#imgg=cv2.HoughCircles(img1,cv2.HOUGH_GRADIENT,dp=1,minDist=40
                        #,param1=45,param2=25,minRadius=15,maxRadius=35)
imgg=cv2.HoughCircles(img1,cv2.HOUGH_GRADIENT,dp=1,minDist=30
                      ,param1=100,param2=20,minRadius=10,maxRadius=30)

if imgg is None:
    exit(-1)


imgg=np.uint16(np.around(imgg))
print(imgg)    


QTY=0

for i in imgg[0, :]:

    cv2.circle(img, (i[0], i[1]), i[2], (0, 111, 0), 2)
    cv2.circle(img, (i[0], i[1]), 2, (0, 255, 111), 2)    
    QTY+=1
    
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'FIND '+ str(QTY),(10,30), font, 1,(0, 222, 0),2)
    
cv2.imshow("HoughCircles",img)
cv2.waitKey(0)
cv2.destroyAllWindows()