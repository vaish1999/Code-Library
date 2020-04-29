import pandas as pd 
import numpy as np 
import cv2
import pickle

# read train data
xy = pd.read_csv("./kannada_dataset/train.csv")
data = np.array(xy)
labels = data[:,0]
dataset = []

for i in range(len(data)):
    # img = np.reshape(data[i , 1:] , (28 , 28)).astype(np.uint8)
    # cv2.imshow("img",img)
    # cv2.waitKey(0)
    print(i)
    img = (np.reshape(data[i , 1:] , (28 , 28)) / 255).astype(np.float32)
    dataset.append(img)

dataset = np.array(dataset)

# print(type(dataset[2]),type(dataset[3][2][4]))
with open("./kannada_dataset/kmnist_train_img.pkl",'wb') as file:
    pickle.dump(dataset , file)


with open("./kannada_dataset/kmnist_train_lbl.pkl",'wb') as file:
    pickle.dump(labels , file)












#read test data
xy = pd.read_csv("./kannada_dataset/test.csv")
data = np.array(xy)
labels = data[:,0]
dataset = []

for i in range(len(data)):
    # img = np.reshape(data[i , 1:] , (28 , 28)).astype(np.uint8)
    # cv2.imshow("img",img)
    # cv2.waitKey(0)
    print(i)
    img = (np.reshape(data[i , 1:] , (28 , 28)) / 255).astype(np.float32)
    dataset.append(img)

dataset = np.array(dataset)

# print(type(dataset[2]),type(dataset[3][2][4]))
with open("./kannada_dataset/kmnist_test_img.pkl",'wb') as file:
    pickle.dump(dataset , file)


with open("./kannada_dataset/kmnist_test_id.pkl",'wb') as file:
    pickle.dump(labels , file)

