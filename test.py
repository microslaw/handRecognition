#display image from camera

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    print(cap.isOpened())
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    #save image to file
    cv.imwrite('test.jpg', frame)