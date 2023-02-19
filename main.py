import tkinter as tk
from handleModel import predict
from imagePreprocessing import formatImage, laplacianImage
import cv2 as cv
import tkinter as tk
from PIL import Image, ImageTk

black = "#000000"
white = "#ffffff"
blue = "#0000a0"

delay = 20

videoResolution = 512

buttonBorderWidth = 10

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


def updateFrameDisplay(frame):

    image = []
    if videoType == "normal":
        image = cv.resize(frame, (videoResolution, videoResolution))
    elif videoType == "treshold":
        image = formatImage(frame, videoResolution)
    elif videoType == "laplacian":
        image = laplacianImage(frame, videoResolution)

    image = convertToTkinterImage(image)
    imgHolder.configure(image = image)
    imgHolder.image = image
    
def updatePredictionsDisplay(predictions):
    predictionsDisplay.delete("all")
    for i, prediction in enumerate(predictions):
        x0 = 100
        y0= (i+1)*50
        x1 = x0 + 300*prediction
        y1 = (i+1)*50 + 25
        predictionsDisplay.create_rectangle(x0, y0, x1, y1, fill=blue)
        predictionsDisplay.create_text(x0-60, y0+13, text=predictionsDisplay.text[i], anchor="w", fill=white)


def updateUI():
    arrayFrame = getRGBFrame()
    predictions = predict(arrayFrame)
    updateFrameDisplay(arrayFrame)
    updatePredictionsDisplay(predictions)
    mainWindow.after(delay, updateUI)

def setVideoType(type):
    global videoType
    videoType = type
    print("video type reset to %s" % videoType)

def createUI():
    global mainWindow, cap, predictionsDisplay, imgHolder, videoType, videoTypeButtons
    videoType = "normal"
    cap = cv.VideoCapture(0)
    mainWindow = tk.Tk()
    mainWindow.title("Rock Paper Scissors")
    
    imgHolder = tk.Label(mainWindow, width = videoResolution, height = videoResolution, bg=black, anchor="se")
    imgHolder.grid(row = 0, column = 0, rowspan = 2)
    

    predictionsDisplay = tk.Canvas(mainWindow, width = videoResolution, height = videoResolution/2, bg=black)
    predictionsDisplay.grid(row = 0, column = 1, columnspan = 3, sticky="n")
    predictionsDisplay.text = ["Rock", "Paper", "Scissors", "Unknown"]    
    
    videoTypeButtons = {"normal": None, "treshold": None, "laplacian": None}

    videoTypeButtons["normal"] = tk.Button(mainWindow, text="normal", borderwidth = buttonBorderWidth,width=20, height=10, bg = black, fg = white, command=lambda: setVideoType("normal"))
    videoTypeButtons["treshold"] = tk.Button(mainWindow, text="treshold", borderwidth = buttonBorderWidth,width=20, height=10, bg = black, fg = white, command=lambda: setVideoType("treshold"))
    videoTypeButtons["laplacian"] = tk.Button(mainWindow, text="laplacian", borderwidth = buttonBorderWidth,width=20, height=10, bg = black, fg = white, command=lambda: setVideoType("laplacian"))
    
    for i,key in enumerate(videoTypeButtons):
        videoTypeButtons[key].grid(row = 1, column = 1+i, sticky="n")
        
    
    resXres = "%sx%s" % (videoResolution*2+8, videoResolution)
    mainWindow.geometry(resXres)
    mainWindow.configure(bg=black)

createUI()
updateUI()
mainWindow.mainloop()

