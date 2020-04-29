import cv2
import numpy as np 


img=cv2.imread("c:/users/girishhegde/iitdimg/brain.jfif")
gray=cv2.imread("c:/users/girishhegde/iitdimg/brain.jfif",0)
cv2.imshow("brain",img)
print(img)
x,y,z=img.shape


t1=110
t2=140

img1=np.zeros([x,y,3],np.uint8)


for i in range(x):
	for j in range(y):
		img1[i,j]=img[i,j]
		if gray[i,j]>t1 and gray[i,j]<t2:
			img1[i,j,2]=255
			img1[i,j,1]=0
			img1[i,j,0]=0

			

'''
		elif gray[i,j]>t1 and gray[i,j]<t2:
			img1[i,j,1]=255
			img1[i,j,0]=0
			img1[i,j,2]=0
		else:
			img1[i,j,2]=255
			img1[i,j,0]=0
			img1[i,j,1]=0

'''
			


cv2.imshow("segment.jpg",img1)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()