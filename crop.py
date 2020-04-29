import cv2
import numpy as np 


img=cv2.imread("c:/users/girishhegde/th.jpg")

x,y,z=img.shape


vh=np.zeros([x,int(y/2),3],np.uint8)
vh=img[:x,:int(y/2),:3]
hf=np.zeros([int(x/2),y,3],np.uint8)
hf=img[:int(x/2),:y,:3]

x1=int(input("enter the x coordinate>>"))
y1=y-int(input("enter the y coordinate>>"))

img3=np.zeros([100,100,3],np.uint8)
img3=img[x1:x1+100,y1:y1+100,:3]


q1=np.zeros([int(x/2),int(y/2),3],np.uint8)
q1=img[:int(x/2),:int(y/2),:3]
q2=np.zeros([int(x/2),int(y/2),3],np.uint8)
q2=img[int(x/2):int(x),:int(y/2),:3]
q3=np.zeros([int(x/2),int(y/2),3],np.uint8)
q3=img[:int(x/2),int(y/2):int(y),:3]
q4=np.zeros([int(x/2),int(y/2),3],np.uint8)
q4=img[int(x/2):x,int(y/2):int(y),:3]


cv2.imshow("img",img)

cv2.imshow("vh",vh)
#cv2.imwrite("blue.jpg",img1)
cv2.imshow("hf",hf)
#cv2.imwrite("green.png",img2)
cv2.imshow("x,ycrop",img3)
#cv2.imwrite("red.tiff",img3)
cv2.imshow("q2",q1)
#cv2.imwrite("c:/users/girishhegde/iitdimg/gray.jpg",gray)
cv2.imshow("q3",q2)
cv2.imshow("q1",q3)
cv2.imshow("q4",q4)

k=cv2.waitKey(0)
if k==27:
	cv2.destroyAllWindows()