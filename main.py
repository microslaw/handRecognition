import numpy as np
from keras import *
import tensorflow as tf

from trainModel import *

trainImages, trainLabels, testImages, testLabels = loadDataset()
trainModel(trainImages, trainLabels)