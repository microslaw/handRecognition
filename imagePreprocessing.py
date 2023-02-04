import cv2 as cv
import numpy as np


def imagePreprocessing(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    