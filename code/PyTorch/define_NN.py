'''Defining a Neural Network
https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html#define-the-network

'''

import torch
import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):

	def __init__(self):
		super(Net, self).__init__()
		# 1 input image channel, 6 output channels, 5x5 square convolution
		# kernel
		self.conv1 = nn.Conv2d(1, 6, 5)
		self.conv2 = nn.Conv2d(6, 16, 5)
		# an affine operation: y = Wx + b
		self.fc1 = nn.Linear(16 * 5 * 5, 120)
		self.fc2 = nn.Linear(120, 84)
		self.fc3 = nn.Linear(84, 10)

	def forward(self, x):
		# Max pooling over a (2, 2) window
		x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
		# If the size is a square you can only specify a single number
		x = F.max_pool2d(F.relu(self.conv2(x)), 2)
		x = x.view(-1, self.num_flat_features(x))
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		x = self.fc3(x)
		return x

	def num_flat_features(self, x):
		size = x.size()[1:]  # all dimensions except the batch dimension
		num_features = 1
		for s in size:
			num_features *= s
		return num_features

	# loss function
	def mean_sq_error():
		output = net(input)
		target = torch.randn(10)  # a dummy target, for example
		target = target.view(1, -1)  # make it the same shape as output
		criterion = nn.MSELoss()

		print(criterion(output, target))

print('****************************************************')

# initialise instance of NN
net = Net()
print(net)

print('****************************************************')

# learnable parameters of a model are returned by net.parameters()
params = list(net.parameters())
print(len(params))
print(params[0].size())  # conv1's .weight

print('****************************************************')

input = torch.randn(1, 1, 32, 32)
out = net(input)
print(out)

print('****************************************************')

output = net(input)
target = torch.randn(10)  # a dummy target, for example
target = target.view(1, -1)  # make it the same shape as output
criterion = nn.MSELoss()

print(criterion(output, target))

print('****************************************************')


