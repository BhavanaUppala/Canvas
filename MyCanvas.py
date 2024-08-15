from tkinter import *;
import tkinter as tk
from tkinter import colorchooser
window=Tk()

drawing=False
erase=False
x,y=None,None
def start(event):
    global x,y,drawing
    drawing=True
    x,y=event.x,event.y
def draw(event):
    global drawing,x,y
    
    if drawing:
        
        canvas.create_line(x,y,event.x,event.y,fill="green")
        x,y=event.x,event.y


def stop(event):
    global drawing
    drawing=False


def starterase(event):
    global erase,x,y
    erase=True
    if erase :
        canvas.create_line(x,y,event.x,event.y,fill="white")
        x,y=event.x,event.y
        



def stop_erase(event):
    global erase
    erase=False
window.title("smartcalculator")
def btn_press(event):
    global x,y
    x=event.x
    y=event.y
    

def click():
    canvas.configure(bg=colorchooser.askcolor()[1])


    
canvas=tk.Canvas(window,width=400,height=400,bg="white")
btn=Button(window,text="click",command=click)
btn.pack()
canvas.pack()

canvas.bind("<Button-1>", start) 
canvas.bind("<B1-Motion>", draw) 
canvas.bind("<ButtonRelease-1>", stop) 
canvas.bind("<B3-Motion>",starterase)
canvas.bind("<ButtonRelease-1>",stop_erase)

window.mainloop()

