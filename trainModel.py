import tensorflow as tf
import keras
import numpy as np


trainTestSplit = 0.8


def createModel():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape = (256, 256, 3)),
        keras.layers.Dense(128, activation = tf.nn.relu),
        keras.layers.Dense(4, activation = tf.nn.softmax)
    ])
    model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
    return model

def trainModel(trainImages, trainLabels):
    model = createModel()
    model.fit(x = trainImages, y = trainLabels, epochs = 5, batch_size = 50)
    model.save("v1.h5")
    

def loadDataset():
    images = np.load("data/trainImages.npy")
    labels = np.load("data/trainLabels.npy")
    trainImages = images[:int(len(images)*trainTestSplit)]
    trainLabels = labels[:int(len(labels)*trainTestSplit)]
    testImages = images[int(len(images)*trainTestSplit):]
    testLabels = labels[int(len(labels)*trainTestSplit):]
    return trainImages, trainLabels, testImages, testLabels

trainImages, trainLabels, testImages, testLabels = loadDataset()
trainModel(trainImages, trainLabels)