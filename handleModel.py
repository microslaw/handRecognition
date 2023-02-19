from keras import models
from imagePreprocessing import *
model = models.load_model("v1.h5")

def predict(image):
    bitmap = formatImage(image, 32)
    bitmap = bitmap.reshape(1, 32, 32, 1)
    return model.predict(bitmap)[0]