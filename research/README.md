```bash

# create virtualenv
python3 -m venv ~/git/Msc_Project/code/.venv

# use virtualenv to install pytorch
source .venv/bin/activate

# install pytorch
pip3 install torch torchvision

```

=== 

following info from - `https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html#define-the-network`

A typical training procedure for a neural network is as follows:

* Define the neural network that has some learnable parameters (or weights)
* Iterate over a dataset of inputs
* Process input through the network
* Compute the loss (how far is the output from being correct)
* Propagate gradients back into the network’s parameters
* Update the weights of the network, typically using a simple update rule: weight = weight - learning_rate * gradient

*`torch.nn` only supports mini-batches, and not a single sample.  
If you have a single sample, just use `input.unsqueeze(0)` to add a fake batch dimension.*  

Loss Function : A loss function takes the (output, target) pair of inputs, and computes a value that estimates how far away the output is from the target.  

===

following info from - `https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py`

Load and normalizing the CIFAR10 training and test datasets using torchvision
* Define a Convolution Neural Network
* Define a loss function
* Train the network on the training data
* Test the network on the test data