import cv2
import numpy as np 



img=np.zeros((500,500),np.uint8)
#cv2.imshow("img",img)

xl=499
yl=499

x1=0
y1=0
x2=400
y2=250


dx=x2-x1
dy=y2-y1

m=dy/dx
j=y1
#img[1,480]=255
for i in range(x1,x2):
	img[yl-j,i]=255
	j=round(j+m)


cv2.imshow("dda",img)



cv2.waitKey(0)
cv2.destroyAllWindows()


