import cv2
import matplotlib.pyplot as plt 
import numpy as np


gray=cv2.imread("c:/users/girishhegde/dog.jpg",0)
cv2.imshow('gray',gray)
cv2.imwrite("gray.jpg",gray)
base=cv2.imread("c:/users/girishhegde/dog.jpg")
cv2.imshow("base",base)
cv2.imwrite("base.jpg",base)

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

	hmi=np.zeros([256,1000])     #target histogram index array
	yi=np.zeros(256)             #y index => no.of pixels producing same intesity ofter equalization

	#plt.subplot(2,1,1)
	#plt.bar([i for i in range(256)],hm)

	#plt.bar(range(256),hm)
	#plt.show()

	for i in range(256):
		hmi[int(hm[i]),int(yi[int(hm[i])])]=i   #inverse histogram of target
		yi[int(hm[i])]+=1

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



			temp[i,j]=hmi[index][yindex]  #remapping pixels

	return temp



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



def paint(ipimg,base,rgbbase):

	m,n=ipimg.shape
	m2,n2=base.shape


	temp=np.zeros((m,n,3),np.uint8)

	sdi=sd(ipimg)
	sdt=sd(base)

	for i in range(m):
		for j in range(n):
			print(i,j)
			f=0
			for k in range(m2):
				for l in range(n2):

					if ipimg[i,j]==base[k,l]:
						if f==0:
							sm=sdt[k,l]
							K=k
							L=l
							f=1
						else:
							if sdt[k,l]<sm:
								sm=sdt[k,l]
								K=k
								L=l


			temp[i,j]=rgbbase[K,L]

	return temp



labbase=cv2.cvtColor(base,cv2.COLOR_BGR2Lab)
cv2.imshow("lab-l",labbase[:labbase.shape[0],:labbase.shape[1],0])
cv2.imwrite("lab.jpg",labbase[:labbase.shape[0],:labbase.shape[1],0])

#out=histmatch(gray,labbase[0])
#cv2.imshow('histmatch',out)

out=gray


color=paint(out,labbase[:labbase.shape[0],:labbase.shape[1],0],base)
cv2.imshow("colored",color)
cv2.imwrite("colored.jpg",color)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
		