import numpy as np
import os
import cv2 as cv

from imagePreprocessing import *

resolution = 32

data = []
labels = []
for file in os.listdir("data"):
    if file.endswith(".jpg"):
        img = cv.imread("data/" + file)
        img = formatImage(img, resolution)
        img = img.flatten()
        data.append(img)
        labels.append(file.split("_")[0])

np.save('data.npy', data)
np.save('labels.npy', labels)
