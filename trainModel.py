import tensorflow as tf
import keras
import numpy as np


trainTestSplit = 0.8


def createModel():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape = (32, 32)),
        keras.layers.Dense(128, activation = tf.nn.relu),
        keras.layers.Dense(4, activation = tf.nn.softmax)
    ])
    model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
    return model

def trainModel(trainImages, trainLabels):
    model = createModel()
    print(trainImages.shape, trainLabels.shape)
    model.fit(x = trainImages, y = trainLabels, epochs = 5, batch_size = 50)
    model.save("v1.h5")
    

def loadDataset():
    images = np.load("images.npy")
    labels = np.load("labels.npy")
    trainImages = images[:int(len(images)*trainTestSplit)]
    trainLabels = labels[:int(len(labels)*trainTestSplit)]
    testImages = images[int(len(images)*trainTestSplit):]
    testLabels = labels[int(len(labels)*trainTestSplit):]
    print("loaded")
    print(trainImages.shape, trainLabels.shape)
    print("size returned")
    
    return trainImages, trainLabels, testImages, testLabels