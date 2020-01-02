# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 03:44:25 2019

@author: s7871
"""

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\s7871\\Pictures\\6.png",cv2.IMREAD_GRAYSCALE)
imgg=np.array(
        [[1.6,0,-150],
        [0,1.6,-200]],
        dtype=np.float32)

imggg=cv2.warpAffine(img,imgg,(200,200))
cv2.imshow('1',imggg)
cv2.waitKey(0)
cv2.EV

