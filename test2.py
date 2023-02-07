import tkinter as tk
import cv2
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)
success, frame = cap.read() 

mainWindow = tk.Tk(screenName="Camera Capture")
lmain = tk.Label(mainWindow)
lmain.pack()

def getRGB(cap):

    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    return cv2image


def update():
    cv2image = getRGB(cap)
    prevImg = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=prevImg)
    lmain.cokolwiek = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, update)

update()
mainWindow.mainloop()