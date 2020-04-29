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

bsize = 100

validation = .1

class to_dataset(Dataset):

    def __init__(self , data ,lbl):
        self.len = lbl.shape[0]
        self.x_data = from_numpy(data)
        self.y_data = from_numpy(lbl)

    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]

    def __len__(self):
        return self.len

#read train data
#xy = pd.read_csv("../kannada/train.csv")
#data = np.array(xy)

with open('./kannada_dataset/kmnist_test_img.pkl','rb') as file:
    data = pickle.load(file)

with open('./kannada_dataset/kmnist_test_id.pkl','rb') as file:
    ids = pickle.load(file)


imgs = data.copy()
data = data.reshape(5000, 1, 28, 28)
dataset = to_dataset(data , ids)

data = torch.from_numpy(data)
test_loader = DataLoader(dataset    = dataset ,
                          batch_size = bsize   ,
                          shuffle    = True    )

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
        #to 1d
        x = x.view(in_size, -1) 
        x = self.fc(x)
        
        #return F.log_softmax(x)

        return x


model = Net()


criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


if torch.cuda.is_available():
    model = model.cuda()
    criterion = criterion.cuda()

print(model)


model.load_state_dict(torch.load("./kannada_dataset/weights.pt"))
model.eval()

with torch.no_grad():
    output = model(data.cuda())

softmax = torch.exp(output).cpu()
prob = list(softmax.numpy())
predictions = np.argmax(prob, axis=1)

# kernels = model.conv1.weight.detach()
# fig , axarr = plt.subplots(kernels.size(0))
# for i in range(kernels.size(0)):
#     axarr[i].imshow(kernels[i].squeeze())


font = cv2.FONT_HERSHEY_SIMPLEX 
  


org = (10, 30)
fontScale = 1
color = 255 
thickness = 1


for i in range(20):
    #idx = i
    idx = np.random.randint(5000)
    image = cv2.resize((imgs[idx] * 255).astype(np.uint8) , (28*10,28*10))
    img = cv2.putText(image, str(predictions[idx]), org, font,  
                   fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("img",img)
    # cv2.imwrite("./output%d.png"%i , img)
    # print(i)
    #print(predictions[idx])
    cv2.waitKey(0)

rows = []
rows.append(['id','label'])
for iD,gp in enumerate(list(predictions)):
    rows.append([iD,gp])

csvfile=open('./kannada_dataset/classifiedcsv.csv','w',newline = "")
writer = csv.writer(csvfile)
writer.writerows(rows)
csvfile.close()

