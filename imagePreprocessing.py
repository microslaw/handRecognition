import cv2 as cv
import numpy as np

#grayscale, blur, 
def simplifyImage(image):
    kernel = np.ones((5, 5), np.uint8)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    
    closed = cv.morphologyEx(blurred, cv.MORPH_CLOSE, kernel)
    opened = cv.morphologyEx(closed, cv.MORPH_OPEN, kernel)

    return opened

def tresholdImage(image):
    treshold = cv.adaptiveThreshold(image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 3)
    return treshold

def laplacianImage(image):
    laplacian = cv.Laplacian(image, cv.CV_64F)
    return laplacian
