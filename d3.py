import numpy as np  
import cv2
import random


#k=int(input("enter the dimension of kernal >>"))
k=3
p=k
q=k
filtr=[[-1,-2,-1],[0,0,0],[1,2,1]]
filtr=np.array(filtr)
print(filtr)

img=cv2.imread('c:/users/girishhegde/iitdimg/sud.jfif',0)
cv2.imshow("img",img)




m,n=img.shape

x=m
y=n


img1=np.zeros([x-2,y-2],np.uint8)

img3=np.zeros([x-2,y-2],np.uint8)

for i in range(0,x-3):
	for j in range(0,y-3):
		s0=0
		s1=0
		s2=0
		for a in range(p):
			for b in range(q):
				s0=s0+img[i+a,j+b]*filtr[a,b]

		img1[i,j]=int(s0)



	
img2=cv2.Sobel(img,cv2.CV_8U,0,1,ksize=3)


dif=np.zeros((x-k,y-k),np.uint8)
for i in range(x-k):
	for j in range(y-k):
		dif[i,j]=((img1[i,j]-img2[i,j])**2)**0.5

cv2.imshow("sobel",img1)
cv2.imshow("sobelinbuilt",img2)
cv2.imshow("withoutdif",dif)

for i in range(m-k):
    for j in range(n-k):
    	#if img1[i,j]>=0 and img1[i,j]<150:
    	#	img1[i,j]=0
    	if img1[i,j]>=200:
    		img1[i,j]=0




dif2=np.zeros((x-k,y-k),np.float32)
for i in range(x-k):
	for j in range(y-k):
		dif2[i,j]=((img1[i,j]-img2[i,j])**2)**0.5
dif2=np.array(dif2,dtype=np.uint8)

cv2.imshow("sobelwiththresholding",img1)
cv2.imshow("differencethreshold",dif2)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



