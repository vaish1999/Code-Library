import cv2
import matplotlib.pyplot as plt 
import numpy as np


img=cv2.imread("c:/users/girishhegde/iitdimg/lena1.tiff",0)
cv2.imshow('img1',img)

tar=cv2.imread("c:/users/girishhegde/iitdimg/lena.tif",0)
cv2.imshow("original",tar)

def equhist(ipimg):

	x,y=ipimg.shape

	temp=np.zeros(ipimg.shape,np.uint8)

	h=np.zeros(256)

	for  i in range(x):
		for j in range(y):
			h[ipimg[i][j]]=h[ipimg[i][j]]+1
	H=h.copy()

	#plt.subplot(2,1,1)
	#plt.bar([i for i in range(256)],h)
	
	#plt.show()
	
	h=h/(x*y)

	for  i in range(1,256): 
		h[i]=h[i]+h[i-1]

	h=h*255

	#plt.subplot(2,1,2)
	#plt.bar([i for i in range(256)],h)
	#plt.show()

	for  i in range(x):
		for j in range(y):
				temp[i][j]=h[ipimg[i][j]]


	return [temp,H,h]


def histmatch(ipimg,compimg):

	x,y=ipimg.shape

	temp,Hi,hi=equhist(ipimg)

	temp2,Hm,hm=equhist(compimg)
	

	plt.bar(range(256),Hi)
	plt.show()
	plt.bar(range(256),hi)
	plt.show()
	plt.bar(range(256),Hm)
	plt.show()
	plt.bar(range(256),hm)
	plt.show()




	hmi=np.zeros([256,1000])     #target histogram index array
	yi=np.zeros(256)             #y index => no.of pixels producing same intesity ofter equalization

	#plt.subplot(2,1,1)
	#plt.bar([i for i in range(256)],hm)

	#plt.bar(range(256),hm)
	#plt.show()

	for i in range(256):
		hmi[int(hm[i]),int(yi[int(hm[i])])]=i   #inverse histogram of target
		yi[int(hm[i])]+=1
		print(yi[int(hm[i])])

	#plt.bar(range(256),hmi[:256,0])
	#plt.show()

	#plt.subplot(2,1,2)
	#plt.bar([i for i in range(256)],hmi)

	for  i in range(x):
		for j in range(y):
			if yi[temp[i,j]]==0:
				if temp[i,j]>127:
					f=0
					for k in range(256-temp[i,j]):
						if (yi[temp[i,j]+k]) !=0:#math the pixel intensity
							index=temp[i,j]+k
							f=1
						if (yi[temp[i,j]-k]) !=0:
							index=temp[i,j]-k
							f=1

					if f==0:
						for k in range(0,256-temp[i,j]):

							if (yi[temp[i,j]-k]) !=0:#math the pixel intensity
								index=temp[i,j]-k


				else:

					f=0
					for k in range(temp[i,j]):
						if (yi[temp[i,j]+k]) !=0:#math the pixel intensity
							index=temp[i,j]+k
							f=1
						if (yi[temp[i,j]-k]) !=0:
							index=temp[i,j]-k
							f=1

					if f==0:
						for k in range(temp[i,j],256-temp[i,j]):

							if (yi[temp[i,j]+k]) !=0:#math the pixel intensity
								index=temp[i,j]+k

			else:
				index=temp[i,j]


			if yi[index]>1:
				li=0
				M=int((ipimg[i,j]-int(hmi[index][0]))**2)**0.5
				for l in range(index):
					m=int((ipimg[i,j]-int(hmi[index][l]))**2)**0.5#if more than 1 match => find distance and select least distant pixel
					if m<M:
						M=m
						li=l
				yindex=li


			else:
				yindex=0



			temp[i,j]=hmi[index,yindex]  #remapping pixels

	return temp



out=histmatch(tar,img)
cv2.imshow('hist',out)
cv2.imwrite("histmatch.jpg",out)

a,b,c=equhist(out)
cv2.imshow('hista',a)
e,f,g=equhist(img)

cv2.imshow('histe',e)
plt.subplot(2,1,1)
plt.bar(range(256),b)
plt.subplot(2,1,2)
plt.bar(range(256),f)
plt.show()
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
		