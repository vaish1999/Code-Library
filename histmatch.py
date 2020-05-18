import cv2
import numpy as np 
import matplotlib.pyplot as plt 


img1=cv2.imread("c:/users/girishhegde/dog.jpg")
img2=cv2.imread("c:/users/girishhegde/dog.jpg",0)


lab=cv2.cvtColor(img1,cv2.COLOR_BGR2Lab)

hic=cv2.equalizeHist(lab[0])

histcolor=np.zeros(256,np.uint8)

for i in range(256):
	histcolor[hic[i]]=histcolor[hic[i]]+1
plt.subplot(2,1)
plt.bar(range(256),histcolor)

hig=cv2.equalizeHist(img2)

histgray=np.zeros(256,np.uint8)


for i in range(256):
	histgray[hic[i]]=histgray[hic[i]]+1
plt.subplot(2,2)
plt.bar(range(256),histgray)


cv2.imshow("hist",hig)