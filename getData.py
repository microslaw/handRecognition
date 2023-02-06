import cv2 as cv
import numpy as np
import tkinter as tk
from imagePreprocessing import *
from PIL import Image, ImageTk

black = "#000000"
white = "#ffffff"
blue = "#0000a0"
global mainWindow
global imgHolder


delay = 10

# take picture from camera
def getRGBFrame():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    ret, frame = cap.read()
    if not ret:
        print("Can not receive frame")
        exit()
    rgbFrame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    return rgbFrame

def createUi():
    global mainWindow, imgHolder
    mainWindow = tk.Tk()
    imgHolder = tk.Label(mainWindow, width = 400, height = 400, bg=blue)
    imgHolder.grid(row = 0, column = 0)

    mainWindow.geometry("800x800")
    mainWindow.configure(bg=black)

    

def updateUi():
    arrayFrame = getRGBFrame()
    frame = Image.fromarray(arrayFrame)
    photo = ImageTk.PhotoImage(image = frame)
    imgHolder.configure(image = photo)
    mainWindow.after(delay, updateUi)

    


createUi()
updateUi()
mainWindow.mainloop()

