# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 14:40:31 2019

@author: s7871
"""

import cv2
import numpy as np

 
img = cv2.imread('C:\\Users\\s7871\\Desktop\\images.jpeg',-1)

img1  = img [ :, : , 0] # 獲取rgb通道中的一個
img2  = img [ :, : , 1] # 獲取rgb通道中的一個
img3  = img [ :, : , 2] # 獲取rgb通道中的一個

print(img.shape)

cv2.imshow("0",img1)
cv2.imshow("01",img2)
cv2.imshow("02",img3)

img = np.float32(img1) # 將數值精度調整爲32位浮點型
img_dct = cv2.dct(img)  # 使用dct獲得img的頻域圖像       
print(img_dct.shape)
cv2.imshow("1",img_dct)

img_recor2 = cv2.idct(img_dct) 
cv2.imshow("2",img_recor2)

cv2.waitKey(0)
cv2.destroyAllWindows()
