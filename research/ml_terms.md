**Machine Learning** - Machine learning is a field of artificial intelligence that uses statistical techniques to give computer systems the ability to "learn" from data, without being explicitly programmed.  

**Neural Network** -  more properly referred to as an 'artificial' neural network (ANN), a computing system made up of a number of simple, highly interconnected processing elements, which process information by their dynamic state response to external inputs - multi layer linear regression   

**Deep Neural Network** - Deep learning neural network architectures differ from "normal" neural networks because they have more hidden layers. Deep learning networks differ from "normal" neural networks and SVMs because they can be trained in an UNSUPERVISED or SUPERVISED manner for both UNSUPERVISED and SUPERVISED learning tasks.  

**Convolutional Neural Network** - a convolutional neural network (CNN, or ConvNet) is a class of deep, feed-forward artificial neural networks, most commonly applied to analyzing visual imagery.  

**Convolution** - convolution is a mathematical operation on two functions (f and g) to produce a third function that expresses how the shape of one is modified by the other.  

**Kernel** - A kernel in a CNN is basically a small window (of say 3 x 3 pixels), that has specific values.   
![Convolution Kernel](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/conv.png)

**SVM** - Support Vector Machine, is a discriminative classifier formally defined by a separating hyperplane. In other words, given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples.  

**Regression Analysis** - used to study the relationship between two or more variables.   

**Neurons* - A "neuron" in an artificial neural network is a mathematical approximation of a biological neuron. It takes a vector of inputs, performs a transformation on them, and outputs a single scalar value. It can be thought of as a filter.   

**Non-saturating Neurons** - A saturated neural network is one where most of the hidden nodes have values close to -1.0 or +1.0 and the output nodes have values close to 0.0 or 1.0. Saturation is not a good thing. If hidden nodes are saturated then that means their pre-activation sum-of-products is relatively large (typically greater than 4.0) or small (typically smaller than -4.0).  

**Hidden Layer** - A hidden layer in an artificial neural network is a layer in between input layers and output layers, where artificial neurons take in a set of weighted inputs and produce an output through an activation function. It is a typical part of nearly any neural network in which engineers simulate the types of activity that go on in the human brain.  

**Tensor** - a mathematical object analogous to but more general than a vector, represented by an array of components that are functions of the coordinates of a space.  
  
**CUDA** - Compute Unified Device Architecture, introduced by Nvidia. The CUDA platform is a software layer that gives direct access to the GPU's virtual instruction set and parallel computational elements, for the execution of compute kernels  

**Pooling Layer** - It is common to periodically insert a Pooling layer in-between successive Conv layers in a ConvNet architecture. Its function is to progressively reduce the spatial size of the representation to reduce the amount of parameters and computation in the network, and hence to also control overfitting.  

**Pooling Layer** - Inserted between successive convolution layers. Its function is to progressively reduce the spatial size of the representation to reduce the amount of parameters and computation in the network, and hence to also control overfitting.  

**Max-pooling** - a sample-based discretization process. The objective is to down-sample an input representation (image, hidden-layer output matrix, etc.), reducing its dimensionality and allowing for assumptions to be made about features contained in the sub-regions binned.    

**Regularization Method** - This is a form of regression, that constrains/ regularizes or shrinks the coefficient estimates towards zero. In other words, this technique discourages learning a more complex or flexible model, so as to avoid the risk of overfitting.  

**Overfitting** - meaning the model predicts well on training data but poorly on new, unseen data.  
![Overfitting](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/overfitting.png)

**ReLU** - Rectified Linear Unit. ReLu refers to the Rectifier Unit, the most commonly deployed activation function for the outputs of the CNN neurons.  

**Tanh** -  Tanh is the hyperbolic tangent function, which is the hyperbolic analogue of the Tan circular function used throughout trigonometry. 
![Tanh & ReLU](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/relu-tanh.png)  

**Gradient Descent** - Gradient descent is an optimization algorithm used to minimize some function by iteratively moving in the direction of steepest descent as defined by the negative of the gradient. In machine learning, we use gradient descent to update the parameters of our model.  
![radient Descent](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/gradient_descent.png)

**Stochastic Gradient Descent** - Stochastic gradient descent (often shortened to SGD), also known as incremental gradient descent, is an iterative method for optimizing a differentiable objective function, a stochastic approximation of gradient descent optimization.  
![Stochastic Gradient Descent](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/stochastic_gradient_d.png)

**Data Augmentation** - Data augmentation means increasing the number of data points. It is a way of creating new 'data' with different orientations.    
 ![Data Augmentation](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/augmented.png)

**PCA** - Principal Component Analysis (PCA) is a dimension-reduction tool that can be used to reduce a large set of variables to a small set that still contains most of the information in the large set.  

**Gaussian Distribution** - It  is a continuous function which approximates the exact binomial distribution of events. The Gaussian distribution shown is normalized so that the sum over all values of x gives a probability of 1.  

**Eigenvalues** - eigenvalues of a linear mapping is a measure of the distortion induced by the transformation  

**Eigenvector** - In linear algebra, an eigenvector or characteristic vector of a linear transformation is a non-zero vector that changes by only a scalar factor when that linear transformation is applied to it.  
![Eigenvector](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/eigen.jpg)

**Backpropogation** - is a method used in artificial neural networks to calculate a gradient that is needed in the calculation of the weights to be used in the network. It is commonly used to train deep neural networks, a term referring to neural networks with more than one hidden layer.  
![Backpropogation](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/backpropogation.png)  

**Derivative** - It is a way to show rate of change: that is, the amount by which a function is changing at one given point  

**Neuron Bias** - values associated with each node in the input and hidden of a network, but in practice are treated in exactly the same manner as other weights. The use of biases in a neural network increases the capacity of the network to solve problems.  

**Learning Rate** - It is a decreasing function of time. Two forms that are commonly used are a linear function of time and a function that is inversely proportional to the time t.   

**Fisher Vectors** - an image representation obtained by pooling local image features, and it is used as a global image descriptor in image classification.  

**Feature Vector** - A feature vector is a representation of an object into a condensed form.  

![Feature Vector](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/featurevector.jpg)

**Autoencoder** - A autoencoder is a neural network that has three layers: an input layer, a hidden (encoding) layer, and a decoding layer. The network is trained to reconstruct its inputs, which forces the hidden layer to try to learn good representations of the inputs.  

![Autoencoder](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/encoder.png)
