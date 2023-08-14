import json
# from turtle import Turtle, Screen
from turtle import Turtle, Screen
from tkinter import *
import time


turtle = Turtle()
screen = Screen()
turtle.showturtle()
turtle.fillcolor('red')

screen.mode('world')

llx = -1230000000
lly = 453000000
urx = -1225000000
ury = 458000000
screen.setworldcoordinates(llx, lly, urx, ury)

screen.tracer(0)


with open('records.json') as f:
    data = json.load(f)


locations = data["locations"]
turtle.penup()
for times in locations:
    turtle.speed(0)
    turtle.width(1)
    timestamp = times["timestamp"]
    # print(timestamp)
    # if "2019-04-23T13:48:06.034Z" < timestamp < "2020-04-23T21:40:21.097Z":
    latitude = times["latitudeE7"]
    longitude = times["longitudeE7"]
    if (llx + 500000) < longitude < (urx + 500000) and (lly - 500000) < latitude < (ury - 500000):
        turtle.goto(longitude, latitude)
        turtle.pendown()
    else:
        turtle.penup()


        screen.update()

screen.exitonclick()