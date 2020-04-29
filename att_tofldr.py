import pandas as pd 
import numpy as np 
import cv2
import os
import random
import pickle

path = './ATT/'

images = os.listdir(path)

positive_dataset = []

for i in range(1,41):
    os.mkdir(path + str(i))

for img in images:
    ig = cv2.imread(path + img, 0)
    fldr = img.split('_')
    cv2.imwrite(path + fldr[0] + './' + fldr[1], ig)





