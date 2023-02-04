import cv2 as cv
import numpy as np
import tkinter as tk
from imagePreprocessing import *
from PIL import Image, ImageTk

black = "#000000"
white = "#ffffff"
blue = "#0000a0"
global mainWindow
global canvas


delay = 10

# take picture from camera
def getFrame():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        exit()
    return frame

def createUi():
    global mainWindow, canvas
    mainWindow = tk.Tk()
    canvas = tk.Canvas(mainWindow, width = 400, height = 400, bg=blue)
    canvas.grid(row = 0, column = 0)

    mainWindow.geometry("800x800")
    mainWindow.configure(bg=black)

    

def updateUi():
    frame = getFrame()
    
    photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
    canvas.create_image(0, 0, image = photo)
    mainWindow.after(delay, updateUi)

    


createUi()
#updateUi()
mainWindow.mainloop()

