import numpy as np  
import cv2
import random


#k=int(input("enter the dimension of kernal >>"))
k=5
p=k
q=k
filtr=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
filtr=np.array(filtr)/25
print(filtr)

img=cv2.imread('c:/users/girishhegde/dog.jpg')
cv2.imshow("img",img)




m,n,c=img.shape


x=m
y=n


img1=np.zeros([x-p+1,y-p+1,3],np.uint8)
img2=np.zeros([x-p+1,y-p+1,3],np.uint8)

img3=np.zeros([x-p+1,y-p+1,3],np.uint8)

for i in range(0,x-p+1):
	for j in range(0,y-q+1):
		s0=0
		s1=0
		s2=0
		for a in range(p):
			for b in range(q):
				s0=s0+img[i+a,j+b,0]*filtr[a,b]
				s1=s1+img[i+a,j+b,1]*filtr[a,b]
				s2=s2+img[i+a,j+b,2]*filtr[a,b]
		img1[i,j,0]=int(s0)
		img1[i,j,1]=int(s1)
		img1[i,j,2]=int(s2)

img2=cv2.blur(img,(5,5))	



for i in range(0,x-p+1):
	for j in range(0,y-q+1):
		img3[i,j]=img1[i,j]-img2[i,j]

cv2.imshow("boxblurmanual",img1)
cv2.imshow("boxblurinbuilt",img2)


m=x-p+1
n=y-p+1
dif=np.zeros((m,n,3),np.uint8)
for i in range(m):
	for j in range(n):
		dif[i,j]=((img1[i,j]-img2[i,j])**2)**0.5
cv2.imshow("dif",dif)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



