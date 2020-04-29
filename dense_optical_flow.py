# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 01:15:44 2019

@author: shashidhar
"""

import cv2
import numpy as np
    def dflow():
    cap = cv2.VideoCapture("3d.mp4")
    ret, frame1 = cap.read()
    prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    flag=0
    temp=0
    z2=0
    count=0
    while(1):
        ret, frame2 = cap.read()
        next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        nx=0
        ny=0
        if (flag == 0):
            x = flow[0]
            y = flow[1]
            x1 = x**2
            y1 = y**2
            z1 = np.sqrt(np.sum(x1)+np.sum(y1))
            flag = 1
            count=count+1
        else:
            x = flow[0]
            y = flow[1]
            
            for i in range(np.shape(x)[0]):
                for j in range(np.shape(x)[1]):
                    if x[i,j]:
                        nx=nx+1
            for i in range(np.shape(x)[0]):
                for j in range(np.shape(x)[1]):
                    if y[i,j]:
                        ny=ny+1
                        
            x1 = x**2
            y1 = y**2
            z2=np.sqrt(np.sum(x1)+np.sum(y1))
                   
            temp = 1
            count=count+1
        print('z1-', z1)
        print('z2-', z2)
        print('z2-z1=', abs(z1-z2))
        c=max(nx,ny)

        if (temp == 1):
            z = (abs(z1 - z2))/c
            print(float(z))
            if (z >0.0 ):
                print("enter 'l' for label or any key to continue")
        
                cv2.imshow('frame',prvs)
                key = cv2.waitKey(0)
                
                if (key == 'l'):
                    label=str(input('enter the label'))
                #if (key==ord('s')):
                    #break
                    
        if temp==1:
            z1=z2
        cv2.imshow('frame',prvs)
        prvs=next
        k=cv2.waitKey(1)
        if k==27:
            break

dflow()
cap.release()
cv2.destroyAllWindows()
   
