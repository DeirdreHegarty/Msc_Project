# https://pythonprogramming.net/introduction-deep-learning-python-tensorflow-keras/

import tensorflow
import matplotlib.pyplot as pyplot

mnist = tensorflow.keras.datasets.mnist #28x28
(x_train, y_train), (x_test, y_test) = mnist.load_data()

pyplot.imshow(x_train[0], cmap=pyplot.cm.binary) # cmap=pyplot.cm.binary - corrects to b&w
# pyplot.show()
# below shows that tensor is a multi dimensional array
# print(x_train[0])

# redefine and normalize to values are scaled between 0 - 1
# do not NEED to do this step
x_train = tensorflow.keras.utils.normalize(x_train, axis=1)
x_test = tensorflow.keras.utils.normalize(x_test, axis=1)

pyplot.imshow(x_train[0], cmap=pyplot.cm.binary)
# pyplot.show()
print(x_train[0]) # images appears 'faded' in parts

# build the model
# There are 2 types of model:
# * sequential - most common,feed forward like image we drew
# change from 28 x 28 multidimensional -> to FLAT

model = tensorflow.keras.models.Sequential()
model.add(tensorflow.keras.layers.Flatten(input_shape = (28,28))) # input layer

model.add(tensorflow.keras.layers.Dense(128, activation=tensorflow.nn.relu)) # units in layer, activation function,
model.add(tensorflow.keras.layers.Dense(128, activation=tensorflow.nn.relu)) # units in layer, activation function,

# output layer will have number of classifications
model.add(tensorflow.keras.layers.Dense(10, activation=tensorflow.nn.softmax)) # softmax - probability

# training of model params
model.compile(optimizer='adam',
			loss='sparse_categorical_crossentropy',
			metrics=['accuracy'])

# train model now
model.fit(x_train, y_train, epochs=3)

# Epoch 1/3
# 2018-10-04 13:26:59.003273: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
# 60000/60000 [==============================] - 4s 61us/step - loss: 0.2607 - acc: 0.9239
# Epoch 2/3
# 60000/60000 [==============================] - 4s 58us/step - loss: 0.1050 - acc: 0.9672
# Epoch 3/3
# 60000/60000 [==============================] - 3s 55us/step - loss: 0.0719 - acc: 0.9774

# calculate the validation loss in validation accuracy
val_loss, val_acc = model.evaluate(x_test, y_test)
print(val_loss, val_acc)

# save model
model.save('keras_tensorflow_model.model')
# load model
# new_model = tensorflow.keras.models.load_model('keras_tensorflow_model.model')
# predictions = new_model.predict([x_test])
# print(predictions)


