import cv2
import numpy as np
import random

img = cv2.imread('sobel.png', 0)


cv2.imshow('img', img)
m, n = img.shape

k = 3

img1 = np.zeros([(m-k)+1, (n-k)+1], np.uint8)

kernel = [[-1, -2, -1], [0,0,0], [1, 2, 1]] #sobel


for i in range(m-k):
    for j in range(n-k):
        s0=0
        s1=0
        s2=0
        for a in range(k):
            for b in range(k):
                s0 = s0 + kernel[a][b]*img[i+a][j+b]

        img1[i][j] = s0

cv2.imshow("conv_img",img1)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()



