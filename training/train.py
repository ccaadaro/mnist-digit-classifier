from torchvision import datasets, transforms
from torch import nn, optim
import torch
from model import Net

transform = transforms.ToTensor()
trainset = datasets.MNIST('.', download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

model = Net()
optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

for epoch in range(50):
    for images, labels in trainloader:
        optimizer.zero_grad()
        output = model(images)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()

torch.save(model.state_dict(), '../api/model.pt')