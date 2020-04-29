import cv2
import numpy as np 

x=cv2.imread("house.tif")
img=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
img=np.float32(img)

dst=cv2.cornerHarris(img,2,3,0.04)
dst=cv2.dilate(dst,None)
x[dst>0.01*dst.max()]=[0,0,255]

cv2.imshow("img",x)
#cv2.imshow("corner",dst)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()