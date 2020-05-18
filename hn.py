import cv2
import matplotlib.pyplot as plt 
import numpy as np


img=cv2.imread("dog2.jpg",0)
cv2.imshow('dog',img)

h=np.zeros(256,np.float32)

x,y=img.shape


img1=np.zeros((x,y),np.uint8)

img2=np.zeros((x,y),np.uint8)

img3=np.zeros((x,y),np.uint8)
print(x,'x',y)

for  i in range(x):
	for j in range(y):
		h[img[i][j]]=h[img[i][j]]+1

h=h/(x*y)



for  i in range(1,256): 
	h[i]=h[i]+h[i-1]

h=h*255


hc=np.ceil(h)
hf=np.floor(h)
hr=np.round(h)

hc=np.array(hc,np.uint8)
hf=np.array(hf,np.uint8)
hr=np.array(hr,np.uint8)



plt.bar([i for i in range(256)],hc)
plt.show()
plt.bar([i for i in range(256)],hf)
plt.show()
plt.bar([i for i in range(256)],hr)
plt.show()





for  i in range(x):
	for j in range(y):
		img1[i][j]=hc[img[i][j]]
		img2[i][j]=hf[img[i][j]]
		img3[i][j]=hr[img[i][j]]
			#img[i][j]=h[img[i][j]]
print('done')

img4=cv2.equalizeHist(img)


cv2.imshow('histceil',img1)
cv2.imshow('histfloor',img2)
cv2.imshow('histround',img3)
cv2.imshow('histcv',img4)

cr=0.0
cf=0.0
cc=0.0
for  i in range(x):
	for j in range(y):
		cc=cc+((img4[i,j]-img1[i,j])**2)/(x*y)
		cf=cf+((img4[i,j]-img2[i,j])**2)
		cr=cr+((img4[i,j]-img3[i,j])**2)

cc=cc/(x*y)
cc=cc**0.5

cf=cf/(x*y)
cf=cf**0.5

cr=cr/(x*y)
cr=cr**0.5

print("cc",cc)
print("cf",cf)
print("cr",cr)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
