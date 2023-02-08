import cv2 as cv
import numpy as np
import tkinter as tk
from imagePreprocessing import *
from PIL import Image, ImageTk

black = "#000000"
white = "#ffffff"
blue = "#0000a0"

delay = 10

videoResolution = 256

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

    images["normal"] = cv.resize(arrayFrame, (videoResolution, videoResolution))
    images["treshold"] = formatImage(arrayFrame, videoResolution)
    images["laplacian"] = laplacianImage(arrayFrame, videoResolution)
    
    for key, image in images.items():
        images[key] = convertToTkinterImage(image)
    
    imgHolder1.configure(image = images["normal"])
    imgHolder1.image = images["normal"]

    imgHolder2.configure(image = images["treshold"])
    imgHolder2.image = images["treshold"]

    imgHolder3.configure(image = images["laplacian"])
    imgHolder3.image = images["laplacian"]
    
    mainWindow.after(delay, updateUi)

def saveFrame():
    saveFrame.count += 1
    arrayFrame = getRGBFrame()
    filepath = "frame%d.jpg" % (saveFrame.count)
    print(filepath)
    cv.imwrite(filepath, arrayFrame)
saveFrame.count = 0

cap = cv.VideoCapture(0)
mainWindow = tk.Tk()
imgHolder1 = tk.Label(mainWindow, width = videoResolution, height = videoResolution, bg=blue)
imgHolder1.grid(row = 0, column = 0)
imgHolder2 = tk.Label(mainWindow, width = videoResolution, height = videoResolution, bg=blue)
imgHolder2.grid(row = 0, column = 1)
imgHolder3 = tk.Label(mainWindow, width = videoResolution, height = videoResolution, bg=blue)
imgHolder3.grid(row = 1, column = 0)
saveButton = tk.Button(mainWindow, text = "Save", width = 50, height = 10, bg=blue, anchor="se", command = saveFrame)
saveButton.grid(row = 1, column = 1)

resXres = "%sx%s" % (videoResolution*2, videoResolution*2)
mainWindow.geometry(resXres)
mainWindow.configure(bg=black)


updateUi()
mainWindow.mainloop()

