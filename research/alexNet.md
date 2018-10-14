# AlexNet:
* AlexNet famously won the 2012 ImageNet LSVRC-2012 competition by a large margin (15.3% VS 26.2% (second place) error rates).
* Non-linear (Use Relu instead of Tanh)
  * `Relu` - rectified linear unit, most used activation function in the world right now, the rectifier is an activation function defined as the positive part of its argument
  * `Tanh` - mainly used classification between two classes
* Use dropout instead of regularisation to deal with overfitting
* Overlap pooling to reduce the size of network

#### The Architecture
* 5 convolutional layers
* 3 fully connected layers 
* Relu is applied after very convolutional and fully connected layer
* Dropout is applied before the first and the second fully connected 
* The image size 227 * 227 (instead of 224 * 224)

![Image from AlexNet paper](https://github.com/DeirdreHegarty/Msc_Project/blob/master/images/alex_net1.png)




# Papers
`https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks`  
