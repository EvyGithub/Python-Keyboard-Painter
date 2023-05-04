import turtle as t
import time
from tkinter import messagebox
import os

# Setup
t.setup(750, 750)
t.pensize(3) # Default but can be changed
t.title("Keyboard Painter")

os.remove("log.txt")
with open("log.txt", "w"):
    pass

# Variables (All caps means they SHOULDN'T be changed)
speed = 3

# Functions
def goUp():
    t.speed(0)
    t.seth(90)
    t.speed(speed)
    t.fd(30) 

def goDown():
    t.speed(0)
    t.seth(270)
    t.speed(speed)
    t.fd(30)

def goLeft():
    t.speed(0)
    t.seth(180)
    t.speed(speed)
    t.fd(30)
    
def goRight():
    t.speed(0)
    t.seth(0)
    t.speed(speed)
    t.fd(30)
    
def clear():
    t.clear()
    
def erase():
    t.pencolor("#FFFFFF")

def black():
    t.pencolor("#000000")

def reset():
    t.speed(0)
    t.goto(0, 0)
    t.clear()
    t.speed(speed)

def bFill():
    t.begin_fill()
def eFill():
    t.end_fill()

def writeText():
    text = t.textinput("Keyboard Painter", "Text?")
    fontSize = t.numinput("Keyboard Painter", "Font size?", default=16, minval=1, maxval=128)
    font = t.textinput("Keyboard Painter", "Font? (Leave blank for Arial)")

    try:
        fontSize = int(fontSize)
    except:
        with open("log.txt", "w") as filedata:
            filedata.write("[Error] Font size must be integer!\n")

    # messagebox.askquestion("Idk", "What?")
    t.write(text, align="center", font=(font, fontSize, "normal"))

# Everything else    
t.listen()

# Keys

# Movement
t.onkey(goUp, "Up")
t.onkey(goDown, "Down")
t.onkey(goLeft, "Left")
t.onkey(goRight, "Right")

# Colors
t.onkey(erase, "e")
t.onkey(black, "t")

t.onkey(bFill, "w")
t.onkey(eFill, "s")

# Misc
t.onkey(clear, "c")
t.onkey(reset, "a")

t.onkey(writeText, "x")

# Loop
t.mainloop()
