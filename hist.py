import cv2
import matplotlib.pyplot as plt 
import numpy as np 

img=cv2.imread("c:/users/girishhegde/img1.jpg",0)
cv2.imshow('img1',img)

h=np.zeros(256)

x,y=img.shape

print(x,'x',y)

for  i in range(x):
	for j in range(y):
		h[img[i][j]]=h[img[i][j]]+1
H=h


h=h/(x*y)


for  i in range(1,256): 
	h[i]=h[i]+h[i-1]

h=h*255
plt.subplot(2,1,1)
plt.title("histogram")
plt.bar([i for i in range(256)],H)
plt.subplot(2,1,2)
plt.title("afyer equalization")
plt.bar([i for i in range(256)],h)
plt.show()

for  i in range(x):
	for j in range(y):
			img[i][j]=h[img[i][j]]
print('done')

cv2.imshow('hist',img)
k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()
