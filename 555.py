# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 04:18:34 2019

@author: s7871
"""

import cv2


img = cv2.imread("C:\\Users\\s7871\\Pictures\\6.png",cv2.IMREAD_COLOR)
b,g,r=cv2.split(img)#拆分
img2=cv2.merge([b,g,r])#合并'