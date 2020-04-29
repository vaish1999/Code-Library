import numpy as np 
import cv2
from mpl_toolkits.mplot3d import Axes3D  
import matplotlib.pyplot as plt
import math

def generate_gaussian_kernal(k = 3 , sigma = 0.8):
	
	#k = a + (n-1)d
	n = ((k - 1) / 2)

	#print(n)

	X = np.arange(-n,n + 1) 

	#print(X)

	Y = X.copy()

	xx,yy = np.meshgrid(X,Y)

	z = np.zeros((X.shape[0],Y.shape[0]),np.float64)

	for i in range(X.shape[0]):
		for j in range(Y.shape[0]):
			z[i,j] = gauss(X[i],Y[j], sigma)

	z = (1/((2*math.pi)**0.5)*sigma) * z

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.plot_surface(xx, yy, z,rstride=1, cstride=1, cmap=plt.cm.inferno,linewidth=1)

	ax.set_xlabel('i')
	ax.set_ylabel('j')
	ax.set_zlabel('gauss')

	plt.show()

	return z

def gauss(x,y,sigma = 0.8):
	return  math.exp( - (x**2 + y**2) / (2 * (sigma ** 2)))
	

kernal = generate_gaussian_kernal(k = 101 , sigma = 20)
print(kernal)
#generate_gaussian_kernal()