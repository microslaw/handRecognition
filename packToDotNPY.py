import numpy as np
import os
import cv2 as cv
from imagePreprocessing import *

resolution = 32

images = np.zeros((0, resolution, resolution), dtype=np.float32)
labels = np.zeros((0), dtype=np.int32)
labelsToOutputs = {"paper": 1, "rock": 0, "scissors": 2, "unknown": 3}
dataLabelList = []

for file in os.listdir("data"):
    if file.endswith(".jpg"):
        img = cv.imread("data/" + file)
        img = formatImage(img, resolution)
        label = labelsToOutputs[file.split("_")[0]]
        images = np.append(images, [img],0)
        labels = np.append(labels, [label],0)

perm = np.random.permutation(images.shape[0])
images = images[perm]
img = images[0]
            
labels = labels[perm]
np.save('images.npy', images)
np.save('labels.npy', labels)
