import cv2 as cv
import numpy as np
import tkinter as tk

black = "#000000"
white = "#ffffff"

# take picture from camera
def get_frame():
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        exit()
    return frame

def displayUI():
    mainWindow = tk.Tk()
    mainWindow.geometry("1600x1600")
    mainWindow.configure(bg=black)
    mainWindow.mainloop()