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
from scipy.signal import correlate2d, convolve2d
import PIL
import torchvision
import matplotlib as mpl
from collections import defaultdict
import seaborn as sn

bsize = 100

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

with open('./kannada_dataset/kmnist_train_img.pkl','rb') as file:
    data = pickle.load(file)

with open('./kannada_dataset/kmnist_train_lbl.pkl','rb') as file:
    lbl = pickle.load(file)

data = data.reshape(60000, 1, 28, 28)


dataset = to_dataset(data , lbl)

bathes  = int(np.ceil(data.shape[0]/bsize))

#load dataloader with training data
train_loader = DataLoader(dataset    = dataset ,
                          batch_size = bsize   ,
                          shuffle    = True    )

class Net(nn.Module):

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5) 
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5)
        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(320, 10)

    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.mp(self.conv1(x)))
        x = F.relu(self.mp(self.conv2(x)))
        #to 1d i.e reshape
        x = x.view(in_size, -1) 
        x = self.fc(x)
        #return F.log_softmax(x)

        return x


model = Net()


criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)


if torch.cuda.is_available():
    model = model.cuda()
    criterion = criterion.cuda()
    
print(model)


def train(epoch):
    for batch , (data , target) in enumerate(train_loader):

        # data, target = Variable(data), Variable(target)

        #if torch.cuda.is_available():
        data   = data.cuda()
        target = target.cuda()

        optimizer.zero_grad()

        output = model(data)
        loss   = criterion(output , target)
        losses.append(loss)

        loss.backward()
        optimizer.step()


        print('[Epoch , batch] : [', epoch + 1 ,"/", epochs ,"][" , batch + 1 , "/",bathes,"]\tloss : " , loss.item())

losses = []

# model.load_state_dict(torch.load("weights.pt"))
# model.eval()

epochs = 10
for epoch in range(epochs):
    train(epoch)


#torch.save(model.state_dict() , "weights.pt")




















###############################################################################################3
#PLOTING

plt.plot(losses)
plt.ylabel("loss")
plt.xlabel("epoch")
plt.show()
# plt.savefig("trainingloss.png")


correct = 0
total = 0
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
errors_imgs=[]
errors_labels=[]
confusion_matrix = torch.zeros(10, 10)
err_confusion_matrix = torch.zeros(10, 10)
correct_samples={i:None for i in range(10)}
with torch.no_grad():
    for data in train_loader:

        images, labels = data[0].to(device), data[1].to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        errors_imgs.extend(images[predicted != labels])
        errors_labels.extend(zip(predicted[predicted != labels], labels[predicted != labels]))
        
        for i in [i for i in correct_samples if type(correct_samples[i]) != torch.Tensor]:
            ci = images[(predicted == labels) & (i == labels)]
            if ci.shape[0] > 0:
                correct_samples[i] = ci[0]
        for t, p in zip(labels.view(-1), predicted.view(-1)):
            confusion_matrix[t.long(), p.long()] += 1
            if t.long() != p.long():
                err_confusion_matrix[t.long(), p.long()] += 1
errors_imgs=torch.stack(errors_imgs)
errors_labels=np.array([(p.item(), t.item())for p, t in errors_labels])
print('accuracy of the network on the test images: %d %%' % (100 * correct / total))



print('errors: ',len(errors_labels))

df_cm = pd.DataFrame(confusion_matrix.numpy(), range(10), range(10))

plt.figure(figsize = (20,20))
plt.title("confusion_matrix")
sn.set(font_scale=2)
sn.heatmap(df_cm, annot=True,annot_kws={"size": 14}, fmt='g')


df_cm = pd.DataFrame(err_confusion_matrix.numpy(), range(10), range(10))

plt.figure(figsize = (20,20))
plt.title("error_confusion_matrix")
sn.set(font_scale=2)
sn.heatmap(df_cm, annot=True,annot_kws={"size": 14}, fmt='g')

sn.set(font_scale=1)
sn.set_style("whitegrid", {'axes.grid' : False})

f=lambda i, a: ({k: len(v) for k, v in a.items()} if [a[x].append(i) for x in i] else {})

errors=f(errors_labels[:,1],defaultdict(list))


plt.figure(figsize=(6,4))
plt.barh(*zip(*errors.items()))
plt.yticks(range(10))
plt.xlabel('erorrs')
plt.ylabel('labels')
plt.show()

