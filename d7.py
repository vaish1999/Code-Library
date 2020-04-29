import cv2
import matplotlib.pyplot as plt 
import numpy as np
import time


t=time.time()

gray=cv2.imread("c:/users/girishhegde/iitdimg/m23.jpg",0)
gray=cv2.resize(gray,(62,90),interpolation=cv2.INTER_AREA)
cv2.imshow('gray',gray)
print(gray.shape)
cv2.imwrite("gray4.jpg",gray)
base=cv2.imread("c:/users/girishhegde/iitdimg/m1gray.jpg")
base=cv2.resize(base,(62,90),interpolation=cv2.INTER_AREA)
cv2.imshow("base",base)
cv2.imwrite("base4.jpg",base)

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

def histmatch(source,base):

	otype=source.dtype
	oshape=source.shape

	source=source.ravel()
	base=base.ravel()

	s_value,s_index,s_counts=np.unique(source,return_inverse=True,return_counts=True)

	b_value,b_counts=np.unique(base,return_counts=True)

	s=np.cumsum(s_counts).astype(np.float64)
	s/=s[-1]


	b=np.cumsum(b_counts).astype(np.float64)
	b/=b[-1]

	interpolate=np.interp(s,b,b_value)
	interpolate=interpolate.astype(otype)

	return interpolate[s_index].reshape(oshape)


def sd(ipimg):
	k=5
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

	m,n=ipimg.shape

	imgp=np.zeros((m+2*z,n+2*z),np.uint8)
	sdarray=np.zeros((m,n),np.float32)
	
	for i in range(m):#padding
		for j in range(n):
			imgp[i+z,j+z]=ipimg[i,j]

	x=m
	y=n

	for i in range(m):
		for j in range(n):
			cnt=0
			s=[]
			for a in range(-1*(z),(z)+1):
				for b in range(-1*(z),(z)+1):
					s.append(imgp[i+a,j+b])

			sdarray[i,j]=np.std(np.array(s))

	return sdarray



def paint(ipimg,base,rgbbase,ltrans):


	#ltrans=cv2.cvtColor(rgbbase,cv2.COLOR_BGR2Lab)

	m,n=ipimg.shape
	m2,n2=base.shape


	temp=np.zeros((m,n,3),np.uint8)

	sdi=sd(ipimg)
	sdt=sd(base)

	print(m,n)
	K=0
	L=0

	for i in range(m):
		print(i)
		for j in range(n):
			
			#f=0
			sm=100

			for k in range(m2):
				for l in range(n2):



					if ipimg[i,j]==base[k,l]:
						#if f==0:
						#	sm=abs(sdt[k,l]-sdi[i,j])
						#	K=k
						#	L=l
						#	f=1
						#else:
							if abs(sdt[k,l]-sdi[i,j])<sm:
								sm=abs(sdt[k,l]-sdi[i,j])
								K=k
								L=l
			


			temp[i,j,0]=ipimg[i,j]
			temp[i,j,1]=ltrans[K,L,1]
			temp[i,j,2]=ltrans[K,L,2]
			#temp=cv2.cvtColor(temp,cv2.COLOR_LAB2BGR)

	temp=cv2.cvtColor(temp,cv2.COLOR_LAB2BGR)
	#cv2.imshow("dsdss",temp)

	return temp



labbase=cv2.cvtColor(base,cv2.COLOR_BGR2Lab)
cv2.imshow("lab-l",labbase[:labbase.shape[0],:labbase.shape[1],0])
cv2.imwrite("lab4.jpg",labbase[:labbase.shape[0],:labbase.shape[1],0])

#out=histmatch(gray,labbase[:labbase.shape[0],:labbase.shape[1],0])
labbase[:labbase.shape[0],:labbase.shape[1],0]=histmatch(labbase[:labbase.shape[0],:labbase.shape[1],0],gray)
out=gray
#cv2.imshow('histmatch',labbase)
#cv2.imwrite("histmatch4.jpg",out)

#out=gray


color=paint(out,labbase[:labbase.shape[0],:labbase.shape[1],0],base,labbase)
#color=paint(gray,labbase[:labbase.shape[0],:labbase.shape[1],0],base)

cv2.imshow("colored",color)
cv2.imwrite("colored4.jpg",color)


print("Total time=",time.time()-t)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
		