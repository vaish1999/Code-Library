import pandas as pd 
import numpy as np 
import cv2
import os
import random
import pickle

path = './ATT/'

directories = os.listdir(path)

positive_dataset = []
print(directories)
for fldr in directories:
    images = os.listdir(path + fldr)
    print(fldr)
    for img in images:
        img1 = cv2.imread(path + fldr + './' + img, 0)
        for img2_p in images:
            img2 = cv2.imread(path + fldr + './' + img2_p, 0)
            # cv2.imshow("img1", img1)
            # cv2.imshow("img2", img2)
            # cv2.waitKey(0)
            positive_dataset.append(np.array([img1 / 255, img2 /255]))


with open("att_positive_pairs.pkl", 'wb') as file:
    pickle.dump(positive_dataset, file)






