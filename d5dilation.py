import numpy as np  
import cv2
import random


#k=int(input("enter the dimension of kernal >>"))
k=3
p=k
q=k
temp=1
z=1
for t in range(1,100):
	temp=temp+2
	if temp==k:
		z=t
		break

print(z)

imgo=cv2.imread('f://cvg19//789.png',0)
cv2.imshow("img",imgo)


se=[[255,255,255],[255,255,255],[255,255,255]]#structural element
se=np.array(se)

m,n=imgo.shape

img=np.zeros((m+2*z,n+2*z),np.uint8)
#to insert noise
for i in range(m):
	for j in range(n):
		img[i+z,j+z]=imgo[i,j]

cv2.imshow("paddedimg",img)

x=m
y=n


img1=np.zeros([m,n],np.uint8)
img2=np.zeros([m,n],np.uint8)

for i in range(m):
	for j in range(n):
		cnt=0
		for a in range(-1*(z),(z)+1):
			for b in range(-1*(z),(z)+1):
				if img[i+a,j+b]==se[a+1,b+1]:
					cnt=cnt+1
		if cnt==0:
			img1[i,j]=0
		else:
			img1[i,j]=255

for i in range(m):
	for j in range(n):
		cnt=0
		x=0
		for a in range(-1*(z),(z)+1):
			for b in range(-1*(z),(z)+1):
				if img[i+a,j+b]==se[a+1,b+1]:
					cnt=cnt+1

		if cnt==k*k:
			img2[i,j]=255
		else:
			img2[i,j]=0
	
ecv=cv2.erode(imgo,se,iterations=1)

dcv=cv2.dilate(imgo,se,iterations=1)
cv2.imshow("dilationcv",dcv)
cv2.imshow("erosioncv",ecv)

cv2.imshow("dilation",img1)
cv2.imshow("erosion",img2)

x=150
y=224
print(img1.shape,dcv.shape)
dif1=np.zeros((x,y),np.uint8)
dif2=np.zeros((x,y),np.uint8)
for i in range(x):
	for j in range(y):
		dif1[i,j]=((img1[i,j]-dcv[i,j])**2)**0.5
		dif2[i,j]=((img2[i,j]-ecv[i,j])**2)**0.5

cv2.imshow("erosiondifference",dif2)
cv2.imshow("dilatioindif",dif1)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



