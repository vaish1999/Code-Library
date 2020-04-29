import cv2
import numpy as np
import matplotlib.pyplot as plt 



img=cv2.imread("c:/users/girishhegde/iitdimg/house.tif")

imgx=img.copy()
gausian=[imgx]


for i in range(5):
	imgx=cv2.pyrDown(imgx)
	gausian.append(imgx)

imgx=gausian[4]

laplace=[imgx]


for i in range(5,0,-1):
	size=(gausian[i-1].shape[1],gausian[i-1].shape[0])
	up=cv2.pyrUp(gausian[i],dstsize=size)
	lap=cv2.subtract(gausian[i-1],up)
	laplace.append(lap)
	cv2.imshow(str(i),lap)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
