import tkinter as tk
import cv2
from PIL import Image, ImageTk

cap = cv2.VideoCapture(0)
success, frame = cap.read() 

mainWindow = tk.Tk(screenName="Camera Capture")
lmain = tk.Label(mainWindow)
lmain.pack()

def show_frame():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    prevImg = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=prevImg)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
 
show_frame()
mainWindow.mainloop()