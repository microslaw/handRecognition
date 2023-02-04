import cv2 as cv
import numpy as np


def preprocessImage(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    cv.imshow("blur", blur)
    resized = cv.resize(blur, (32,32))

    return resized

