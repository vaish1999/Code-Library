import numpy as np
import cv2
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt

img = cv2.imread("F://mini_project//Dataset//woman_blonde.tif",0)
Z = cv2.resize(img,(100,100),interpolation=cv2.INTER_AREA)

x = np.arange(0,100)

y = np.arange(0,100)

X,Y = np.meshgrid(x,y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z,rstride=1, cstride=1, cmap=plt.cm.inferno,linewidth=1)
#cm.gray,inferno,viridious,Reds


ax.set_xlabel('i')
ax.set_ylabel('j')
ax.set_zlabel('img')

plt.show()