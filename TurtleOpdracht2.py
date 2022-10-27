import turtle
import random
import time

colortable = ["green", "red", "yellow", "black", "white"]
shapetable = ["square", "arrow", "turtle", "triangle", "classic"]

random.shuffle(colortable)
random.shuffle(shapetable)

turtle.setup(500, 500, 0, 0)
turtle.pencolor("#5F76D2")
turtle.fillcolor("#FFFFFF")

times = 0

while times < 2:
    for i in range(5):
        chosencolor = colortable[i]
        chosenshape = shapetable[i]

        turtle.bgcolor(chosencolor)
        turtle.shape(chosenshape)
        turtle.right(1000)
        turtle.forward(100)
    
    times += 1