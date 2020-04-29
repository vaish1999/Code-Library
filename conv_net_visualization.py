from torch.utils.data import Dataset, DataLoader
from torch import from_numpy, tensor
import torchvision
import numpy as np
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
import pandas as pd
import pickle
import cv2 
import csv
import matplotlib.pyplot as plt


with open('./kannada_dataset/kmnist_test_img.pkl','rb') as file:
    data = pickle.load(file)

with open('./kannada_dataset/kmnist_test_id.pkl','rb') as file:
    ids = pickle.load(file)


imgs = data.copy()
data = data.reshape(5000, 1, 28, 28)
data = torch.from_numpy(data)

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(320, 10)

    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.mp(self.conv1(x)))
        x = F.relu(self.mp(self.conv2(x)))
        x = x.view(in_size, -1) 
        x = self.fc(x)
    
        return x


model = Net()


# criterion = nn.CrossEntropyLoss()
# optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


if torch.cuda.is_available():
    model = model.cuda()
    # criterion = criterion.cuda()

print(model)


model.load_state_dict(torch.load("./kannada_dataset/weights.pt"))
model.eval()



# layer visualization


# with torch.no_grad():
#     layer1 = F.relu(model.conv1(data.cuda()))


# with torch.no_grad():
#     layer2 = F.relu(model.conv2(model.mp(layer1.cuda())))


# layer1 = layer1.cpu()
# layer1 = np.array(layer1 * 255)


# layer2 = layer2.cpu()
# layer2 = np.array(layer2 * 255)


# for i in range(20):
#     # print(layer1.shape)
#     o_img = data.cpu()[i][0] * 255
#     # print(o_img.shape)
#     o_img = np.uint8(o_img)
#     o_img = cv2.resize(o_img, (28 * 10, 28*10))
#     cv2.imshow("original_img", o_img)


#     img = np.uint8(layer1[i][np.random.randint(0, 9)])
#     img = cv2.resize(img, (24 * 10, 24*10))
#     cv2.imshow("layer1", img)

#     img2 = np.uint8(layer2[i][np.random.randint(0, 19)])
#     img2 = cv2.resize(img2, (img2.shape[0] * 10, img2.shape[1] * 10))
#     cv2.imshow("layer2", img2)

#     cv2.waitKey(0) 

# cv2.destroyAllWindows()



# kerenel visualization

with torch.no_grad():
    kernels = np.array(model.conv1.weight.cpu()) * 255


for i, kernel in enumerate(kernels):
    kernel = kernel[0] + np.min(kernel[0])
    kernel = (kernel - np.min(kernel)) / (np.max(kernel) - np.min(kernel))
    kernels[i] = kernel * 255

# kernels = np.abs(kernels)
kernels = np.uint8(kernels)

for i, kernel in enumerate(kernels):
    ker = cv2.resize(kernel[0], (500, 500), interpolation = cv2.INTER_AREA)
    cv2.imshow("layer1_kernel_%d"%i, ker)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # print(kernel[0])


with torch.no_grad():
    kernels = np.array(model.conv2.weight.cpu()) * 255

print(kernels.shape)

for i, kernel in enumerate(kernels):
    kernel = kernel[0] + np.min(kernel[0])
    kernel = (kernel - np.min(kernel)) / (np.max(kernel) - np.min(kernel))
    kernels[i] = kernel * 255

kernels = np.uint8(kernels)

for i, kernel in enumerate(kernels):
    ker = cv2.resize(kernel[0], (500, 500), interpolation = cv2.INTER_AREA)
    cv2.imshow("layer_2_kernel_%d_channel_0"%i, ker)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # print(kernel[0])


cv2.destroyAllWindows()
