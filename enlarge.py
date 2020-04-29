import numpy as np  
import cv2
import random


k=int(input("enter the dimension of kernal >>"))
p=k
q=k


img=cv2.imread('c:/users/girishhegde/th.jpg')
cv2.imshow("img",img)

m,n,c=img.shape


x=m
y=n


img1=np.zeros([m*p,y*q,3],np.uint8)
kernal0=np.zeros([p,q],np.uint8)
kernal1=np.zeros([p,q],np.uint8)
kernal2=np.zeros([p,q],np.uint8)

for i in range(0,m):
	for j in range(0,n):
		for l in range(i*p,i*p+p):
			for m in range(j*q,j*q+q):
				img1[l,m,0]=img[i,j,0]
				img1[l,m,1]=img[i,j,1]
				img1[l,m,2]=img[i,j,2]

				


cv2.imshow("enlarged",img1)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



