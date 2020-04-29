import numpy as np  
import cv2


filtr=[[-1, -2, -1],
       [ 0,  0,  0],
       [ 1,  2,  1]]

filtr=np.array(filtr)
print(filtr)

kernel_size = filtr.shape[0]

path = 'f://cvg19/sobel.png'

img = cv2.imread(path, 0)
cv2.imshow("img", img)

m , n = img.shape

p = (kernel_size - 1) // 2

padded_h = m + 2 * p
padded_w = n + 2 * p
padded_img = np.zeros([padded_h, padded_w], np.uint8)
padded_img[p:m + 1, p:n + 1] = img.copy()

out = np.zeros((m,n), np.uint8)

for i in range(padded_h - kernel_size):
	for j in range(padded_w - kernel_size):
		s0 = 0
		for vitr in range(kernel_size):
			for hitr in range(kernel_size):
				s0 = s0 + padded_img[i + vitr, j + hitr] * filtr[vitr, hitr]

		out[i,j]=int(s0)


	


cv2.imshow("convolved", out)

cv2.waitKey(0)
cv2.destroyAllWindows()



