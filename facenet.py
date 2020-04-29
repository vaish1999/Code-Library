from torch.utils.data import Dataset, DataLoader
from torch import from_numpy, tensor
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
import matplotlib.pyplot as plt
import cv2
import time

bsize = 20

class to_dataset(Dataset):

    def __init__(self , data ,lbl):
        self.len = lbl.shape[0]
        self.x_data = from_numpy(data)
        self.x_data = self.x_data.type(torch.FloatTensor)
        self.y_data = from_numpy(lbl)

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len

#read train data
lbl = []

print("reading positive_pairs...")
with open('./att_positive_pairs.pkl','rb') as file:
    pos_data = pickle.load(file)
print("done")

for i in range(len(pos_data)):
    lbl.append(1)

print("reading negative_pairs...")
with open('./att_negative_pairs.pkl','rb') as file:
    neg_data = pickle.load(file)


for i in range(len(neg_data)):
    lbl.append(0)
print("done")


pos_data = np.array(pos_data)
neg_data = np.array(neg_data)
lbl      = np.array(lbl)

pos_data = pos_data.reshape(pos_data.shape[0], pos_data.shape[1], 1, pos_data.shape[2], pos_data.shape[3])

neg_data = neg_data.reshape(neg_data.shape[0], neg_data.shape[1], 1, neg_data.shape[2], neg_data.shape[3])


print("positive_data_shape:", pos_data.shape)
print("negative_data_shape:", neg_data.shape)


print("concatenating...")
data =  np.concatenate((pos_data, neg_data), axis=0)
print("done")

pos_data = None
neg_data = None


print("data_shape:", data.shape)

print("loading dataloader...")
dataset = to_dataset(data , lbl)

bathes  = int(np.ceil(data.shape[0] / bsize))

data = None


#load dataloader with training data
train_loader = DataLoader(dataset    = dataset,
                          batch_size = bsize  ,
                          shuffle    = True   )
print("done")


# visualizing training data
# for batch , (data , target) in enumerate(train_loader):
#     print(batch, target[0])
#     cv2.imshow("img1", np.uint8(np.array(data[0,0,0]) * 255))
#     cv2.imshow("img2", np.uint8(np.array(data[0,1,0]) * 255))
#     cv2.waitKey(0)



class Net(nn.Module):

    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(1,  4, kernel_size = 5) 
        self.conv2 = nn.Conv2d(4,  8, kernel_size = 5)
        self.conv3 = nn.Conv2d(8, 16, kernel_size = 5)
        self.conv4 = nn.Conv2d(120,1, kernel_size = 1)
        self.mp    = nn.MaxPool2d(2)
        self.fc1   = nn.Linear(5376, 128)
        self.fc2   = nn.Linear( 128,  10)

    def forward(self, data):
        ip1 = data[:,0]
        ip2 = data[:,1]
        in_size = ip1.size(0)

        op1 = F.relu(self.mp(self.conv1(ip1))) # 105 - 101 
        op1 = F.relu(self.mp(self.conv2(op1)))
        op1 = F.relu(self.conv3(op1))
        
        # print(x.size())
        #to 1d i.e reshape
        
        op1 = op1.view(in_size, -1)
        # print("size = ", op1.size()) 
        op1 = F.relu(self.fc1(op1))
        op1 = self.fc2(op1)
        # x = self.fc2(x)
        #return F.log_softmax(x)

        in_size = ip2.size(0)

        op2 = F.relu(self.mp(self.conv1(ip2))) # 105 - 101 
        op2 = F.relu(self.mp(self.conv2(op2)))
        op2 = F.relu(self.conv3(op2))
        
        # print(x.size())
        #to 1d i.e reshape
        
        op2 = op2.view(in_size, -1) 
        op2 = F.relu(self.fc1(op2))

        op2 = self.fc2(op2)
        #return F.log_softmax(x)

        return op1, op2


# class ContrastiveLoss(torch.nn.Module):

#     def __init__(self, margin=2.0):
#         super().__init__()
#         self.margin = margin

#     def forward(self, output1, output2, label):
#         distance = (output1 - output2)
#         loss = torch.mean((1 - label) * (distance ** 2) + (label) * (torch.clamp(self.margin - distance, min=0.0) ** 2))
#         return loss

class ContrastiveLoss(torch.nn.Module):

    def __init__(self, margin=2.0):
        super(ContrastiveLoss, self).__init__()
        self.margin = margin

    def forward(self, output1, output2, label):
        euclidean_distance = F.pairwise_distance(output1, output2)
        loss_contrastive = torch.mean((1-label) * torch.pow(euclidean_distance, 2) +
                                      (label) * torch.pow(torch.clamp(self.margin - euclidean_distance, min=0.0), 2))


        return loss_contrastive

model = Net().cuda()
criterion = ContrastiveLoss().cuda()
optimizer = optim.Adam(model.parameters(),lr = 1e-6 )


# optimizer = optim.Adam(model.parameters(), lr=0.01)
    
print(model)


def train(epoch):
    for batch , (data , target) in enumerate(train_loader):

        data   = data.cuda()
        target = target.cuda()

        optimizer.zero_grad()

        output1, output2 = model(data)
        loss   = criterion(output1, output2, target)
        losses.append(loss)

        loss.backward()
        optimizer.step()

        print('[Epoch , batch] : [', epoch + 1 ,"/", epochs ,"][" , batch + 1 , "/",bathes,"]\tloss : " , loss)

losses = []


epochs = 500
start_time = time.time()
for epoch in range(epochs):
    train(epoch)


torch.save(model.state_dict() , "facenet_weights.pt")

end_time = time.time()

print("Trainig time = ", end_time - start_time, " seconds")

# model.load_state_dict(torch.load("facenet_weights.pt"))
# model.eval()


# visualizing training data
for batch , (data , target) in enumerate(train_loader):
    print(batch, target)

    data   = data.cuda()
    output1, output2 = model(data)
    euclidean_distance = F.pairwise_distance(output1, output2)
    print("disimilarity: ", (euclidean_distance.cpu().data.numpy()))

    cv2.imshow("img1", np.uint8(np.array(data[0,0,0].cpu()) * 255))
    cv2.imshow("img2", np.uint8(np.array(data[0,1,0].cpu()) * 255))
    cv2.waitKey(0)

