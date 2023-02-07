import cv2 as cv
import numpy as np
import tkinter as tk
from imagePreprocessing import *
from PIL import Image, ImageTk

black = "#000000"
white = "#ffffff"
blue = "#0000a0"
global mainWindow
global imgHolder1

delay = 10

# take picture from camera
def getRGBFrame():
    global cap
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    ret, frame = cap.read()
    if not ret:
        print("Can not receive frame")
        exit()
    rgbFrame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    return rgbFrame

def convertToTkinterImage(frame):
    frame = Image.fromarray(frame)
    photo = ImageTk.PhotoImage(image = frame)
    return photo
    
def updateUi():
    arrayFrame = getRGBFrame()

    images = dict()

    images["normal"] = arrayFrame
    images["treshold"] = tresholdImage(arrayFrame)
    images["laplacian"] = laplacianImage(arrayFrame)
    
    for key, value in images.items():
        images[key] = convertToTkinterImage(value)
    
    imgHolder1.configure(image = images["normal"])
    imgHolder1.image = images["normal"]

    imgHolder2.configure(image = images["treshold"])
    imgHolder2.image = images["treshold"]

    imgHolder3.configure(image = images["laplacian"])
    imgHolder3.image = images["laplacian"]
    
    mainWindow.after(delay, updateUi)

cap = cv.VideoCapture(0)
mainWindow = tk.Tk()
imgHolder1 = tk.Label(mainWindow, width = 400, height = 400, bg=blue)
imgHolder1.grid(row = 0, column = 0)
imgHolder2 = tk.Label(mainWindow, width = 400, height = 400, bg=blue)
imgHolder2.grid(row = 0, column = 1)
imgHolder3 = tk.Label(mainWindow, width = 400, height = 400, bg=blue)
imgHolder3.grid(row = 1, column = 0)


mainWindow.geometry("800x800")
mainWindow.configure(bg=black)


updateUi()
mainWindow.mainloop()

