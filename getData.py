import cv2 as cv
import numpy as np
import tkinter as tk
import random
from imagePreprocessing import *
from PIL import Image, ImageTk
import pickle

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


def updateFrameDisplay():
    global imgHolder
    arrayFrame = getRGBFrame()

    images = dict()

    images["normal"] = cv.resize(arrayFrame, (videoResolution, videoResolution))
    images["treshold"] = formatImage(arrayFrame, videoResolution)
    images["laplacian"] = laplacianImage(arrayFrame, videoResolution)
    
    for key, image in images.items():
        images[key] = convertToTkinterImage(image)
        imgHolders[key].configure(image = images[key])
        imgHolders[key].image = images[key]
    
    mainWindow.after(delay, updateFrameDisplay)

def saveFrame():
    global handShape
    saveFrame.count += 1
    arrayFrame = getRGBFrame()
    filepath = "data/%s_%d.jpg" % (handShape, saveFrame.count)

    cv.imwrite(filepath, arrayFrame)
    
    countLabel.configure(text = str(saveFrame.count+1))
    nextImage()
    with open("data/count.pickle", "wb") as savePickle:
        pickle.dump(saveFrame.count, savePickle)

with open("data/count.pickle", "rb") as loadPickle:
    saveFrame.count = pickle.load(loadPickle)


def getHandShape():
    handShapes = ["rock", "paper", "scissors", "unknown"]
    tmpHandShapes = handShapes.copy()
    tmpHandShapes.remove(getHandShape.previous)
    toReturn = random.choice(tmpHandShapes)
    getHandShape.previous = toReturn
    return toReturn
getHandShape.previous = "unknown"

def nextImage():
    global handShape
    handShape = getHandShape()
    classLabel.configure(text = handShape)

handShape = getHandShape()

def createUI():
    global mainWindow, cap, imgHolders, saveButton, skipButton, classLabel, countLabel, handShape

    cap = cv.VideoCapture(0)
    mainWindow = tk.Tk()

    imgHolders = {"normal": None, "treshold": None, "laplacian": None}

    imgHolders["normal"] = tk.Label(mainWindow, width = videoResolution, height = videoResolution, bg=black, anchor="se")
    imgHolders["normal"].grid(row = 0, column = 0)
    
    imgHolders["treshold"] = tk.Label(mainWindow, width = videoResolution, height = videoResolution, bg=black, anchor="ne")
    imgHolders["treshold"].grid(row = 1, column = 0, rowspan=4)
    
    imgHolders["laplacian"] = tk.Label(mainWindow, width = videoResolution, height = videoResolution, bg=black, anchor="sw")
    imgHolders["laplacian"].grid(row = 0, column = 1, columnspan=2)

    classLabel = tk.Label(mainWindow, text = handShape, width=10, height=3, bg=blue, fg=white, borderwidth=3, justify="center")
    classLabel.grid(row = 1, column = 1)

    countLabel = tk.Label(mainWindow, text =str(saveFrame.count+1), width=10, height=3, bg=blue, fg=white, borderwidth=3, justify="center")
    countLabel.grid(row = 1, column = 2)

    saveButton = tk.Button(mainWindow, text = "Save", width=10, height=3,  bg=blue, fg=white, borderwidth=3, justify="center", command = saveFrame)
    saveButton.grid(row = 2, column = 1)

    skipButton = tk.Button(mainWindow, text = "Skip", width=10, height=3, bg=blue, fg=white, borderwidth=3, justify="center", command = nextImage)
    skipButton.grid(row = 2, column = 2   )
    
    resXres = "%sx%s" % (videoResolution*2, videoResolution*2)
    mainWindow.geometry(resXres)
    mainWindow.configure(bg=black)

createUI()
updateFrameDisplay()
mainWindow.mainloop()

