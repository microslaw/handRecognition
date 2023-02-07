import cv2 as cv
import numpy as np


def preprocessImage(image, shrink=False):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    cv.imshow("blur", blur)
    if shrink:
        resized = cv.resize(blur, (32,32))

    return resized

def getContours(image):
    contours, hierarchy = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    return contours

def tresholdImage(image):
    treshold = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
    return treshold

def laplacianImage(image):
    laplacian = cv.Laplacian(image, cv.CV_64F)
    return laplacian

