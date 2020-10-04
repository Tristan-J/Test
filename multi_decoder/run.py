import torch
from torch import nn
import torchvision
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 


path_data = './data/'

train = torchvision.datasets.CIFAR10(root=path_data, train=True, download=True)
test = torchvision.datasets.CIFAR10(root=path_data, train=False, download=False)

# print(type(train.__dict__))

cifar_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,0.5,0.5), (0.5,0.5,0.5))
    ])

train.transform = cifar_transform
test.transform = cifar_transform
train.transforms = torchvision.datasets.vision.StandardTransform(cifar_transform)
test.transforms = torchvision.datasets.vision.StandardTransform(cifar_transform)

trainloader = torch.utils.data.DataLoader(train, batch_size=4,
                                            shuffle=True,
                                            num_workers=2)
testloader = torch.utils.data.DataLoader(test, batch_size=4,
                                            shuffle=True,
                                            num_workers=2)

train_iter = iter(trainloader)
images, labels = train_iter.next()
# print(images[0])
# print(labels)

def plot_images(images, labels):
    img_grid = torchvision.utils.make_grid(images, nrow=4, normalize=True)
    np_img = img_grid.numpy().transpose(1,2,0)
    plt.imshow(np_img)

images, labels = train_iter.next()
plot_images(images, labels)