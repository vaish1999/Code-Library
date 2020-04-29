import numpy as np  
import cv2
import random


#k=int(input("enter the dimension of kernal >>"))
k=3
p=k
q=k


img=cv2.imread('c:/users/girishhegde/dog.jpg')
cv2.imshow("img",img)




m,n,c=img.shape

for e in range(0,m,random.randint(1,5)):
	for f in range(0,n,random.randint(1,5)):
		r=np.uint8(random.choice([0,255]))
		img[e,f,0]=r
		img[e,f,1]=r
		img[e,f,2]=r

cv2.imshow("img",img)
#to insert noise

x=m
y=n


img1=np.zeros([x-1,y-1,3],np.uint8)


for i in range(1,x-1):
	for j in range(1,y-1):
		s0=[]
		s1=[]
		s2=[]
		for a in [-1,0,1]:
			for b in [-1,0,1]:
				s0.append(img[i+a,j+b,0])
				s1.append(img[i+a,j+b,1])
				s2.append(img[i+a,j+b,2])
		img1[i,j,0]=int(np.median(np.array(s0)))
		img1[i,j,1]=int(np.median(np.array(s1)))
		img1[i,j,2]=int(np.median(np.array(s2)))

	
img2=cv2.medianBlur(img,3)

cv2.imshow("median",img1)
cv2.imshow("medianinbuilt",img2)



dif=np.zeros((x,y,3),np.uint8)
for i in range(x-1):
	for j in range(y-1):
		dif[i,j]=((img1[i,j]-img2[i,j])**2)**0.5

cv2.imshow("dif",dif)


k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



