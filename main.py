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

        # time.sleep(1)
        screen.update()
        # coordinates = {"latitude": latitude, "longitude": longitude}
        # lat_long.append(coordinates)
    # else:
    #     pass

# print(lat_long)
# min_latitude = min(item["latitude"] for item in lat_long)
# min_longitude = min(item["longitude"] for item in lat_long)
# max_latitude = max(item["latitude"] for item in lat_long)
# max_longitude = max(item["longitude"] for item in lat_long)
# lat_range = max_latitude - min_latitude
# long_range = max_longitude - min_longitude
#
# for item in lat_long:
#     lat = 800 / (item["latitude"] - (min_latitude + 1))
#     long = 800 / (item["longitude"] - (min_longitude + 1))
#     turtle.goto(lat, long)
#     screen.update()

# print(f"Min Long: {min_longitude}, Max Long:{max_longitude}")
# # print(f"Min Lat: {min_latitude}, Max Lat:{max_latitude}")
# print(max_latitude - min_latitude)
# print(max_longitude - min_longitude)
#
#
#
screen.exitonclick()