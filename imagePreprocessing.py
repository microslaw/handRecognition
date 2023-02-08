import cv2 as cv
import numpy as np

#grayscale, blur, 
def simplifyImage(image, resolution=512):
    image = cv.resize(image, (512,512))
    kernel = np.ones((5, 5), np.uint8)

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    
    closed = cv.morphologyEx(blurred, cv.MORPH_CLOSE, kernel)
    opened = cv.morphologyEx(closed, cv.MORPH_OPEN, kernel)
    resized = cv.resize(opened, (resolution, resolution))
    
    return resized

def laplacianImage(image, finalResolution=512):
    simplifyImage(image, finalResolution)
    laplacian = cv.Laplacian(image, cv.CV_32F, ksize = 3)
    abs = np.absolute(laplacian)
    #display
    return abs

def formatImage(image, finalResolution=512):
    image = cv.resize(image, (512,512))
    openKernel = np.ones((3, 3), np.uint8)
    closeKernel = np.ones((15, 15), np.uint8)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    #blurred = cv.GaussianBlur(gray, (3,3), 0)
    treshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3)
    #blurred = cv.GaussianBlur(treshold, (3,3), 0)
    opened = cv.morphologyEx(treshold, cv.MORPH_OPEN, openKernel)
    closed = cv.morphologyEx(opened, cv.MORPH_CLOSE, closeKernel)

    return closed
