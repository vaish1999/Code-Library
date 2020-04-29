import numpy as np  
import cv2
import random


#k=int(input("enter the dimension of kernal >>"))
k=3
p=k
q=k
filtr=[[1,1,1],[1,1,1],[1,1,1]]
filtr=np.array(filtr)/9
print(filtr)

img=cv2.imread('c:/users/girishhegde/dog.jpg')
cv2.imshow("img",img)




m,n,c=img.shape


'''for e in range(0,m,10):
	for f in range(0,n,10):
		img[e,f,0]=np.uint8(random.randint(0,255))
		img[e,f,1]=np.uint8(random.randint(0,255))
		img[e,f,2]=np.uint8(random.randint(0,255))
cv2.imshow("img",img)
'''#to insert noise
x=m
y=n


img1=np.zeros([x-p+1,y-p+1,3],np.uint8)


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

	


cv2.imshow("boxblur",img1)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()



