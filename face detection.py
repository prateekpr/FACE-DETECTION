# -*- coding: utf-8 -*-
"""
Created on Wed May 13 18:57:10 2020

@author: prateek
"""

import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("fc.jpg")
gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,1.05,5)

for (x,y,w,h )in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow('fc', img)
cv2.waitKey(0)    
cv2.destroyAllWindows()