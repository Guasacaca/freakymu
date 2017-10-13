from microbit import *
import music
import random

# display.show(Image.HEART)
# display.scroll("Hello!")
right = 3
down = 6
left = 9
top = 0


def ghostLocation():
    return random.randint(-10, 10), random.randint(-10, 10)


def move(direction, X, Y):
    if(direction == top):
        display.show("T")
        return X, Y+1
    elif(direction == down):
        display.show("D")
        return X, Y-1
    elif(direction == right):
        display.show("R")
        return X-1, Y
    elif(direction == left):
        display.show("L")
        return X+1, Y
    else:
        display.show(Image.ANGRY)
        return X, Y


X, Y = ghostLocation()
compass.calibrate()
needle = ((15 - compass.heading()) // 30) % 12
display.show(Image.ALL_CLOCKS[needle])

while True:
    if button_a.is_pressed():
        X, Y = move(needle, X, Y)
        display.show("S")
    else:
        needle = ((15 - compass.heading()) // 30) % 12
        display.show(Image.ALL_CLOCKS[needle])
