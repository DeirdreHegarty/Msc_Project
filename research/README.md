### PyTorch
```bash

# create virtualenv
python3 -m venv ~/git/Msc_Project/code/.venv

# use virtualenv to install pytorch
source .venv/bin/activate

# install pytorch
pip3 install torch torchvision

```

---

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

---

following info from - `https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html#sphx-glr-beginner-blitz-cifar10-tutorial-py`

Load and normalizing the CIFAR10 training and test datasets using torchvision
* Define a Convolution Neural Network
* Define a loss function
* Train the network on the training data
* Test the network on the test data

---

### Keras
```bash
# install keras
pip3 install keras

# install tensorflow
pip3 install tensorflow

# install Theanos (installed in .venv)
git clone git://github.com/Theano/Theano.git
cd Theano
pip3 install -e .

```
### Current pip list
```bash

absl-py (0.5.0)
astor (0.7.1)
cycler (0.10.0)
gast (0.2.0)
grpcio (1.15.0)
h5py (2.8.0)
Keras (2.2.3)
Keras-Applications (1.0.6)
Keras-Preprocessing (1.0.5)
kiwisolver (1.0.1)
Markdown (3.0.1)
matplotlib (3.0.0)
numpy (1.15.2)
Pillow (5.3.0)
pip (9.0.3)
protobuf (3.6.1)
pyparsing (2.2.2)
python-dateutil (2.7.3)
PyYAML (3.13)
scipy (1.1.0)
setuptools (39.1.0)
six (1.11.0)
tensorboard (1.11.0)
tensorflow (1.11.0)
termcolor (1.1.0)
torch (0.4.1)
torchvision (0.2.1)
Werkzeug (0.14.1)
wheel (0.32.0)

```
