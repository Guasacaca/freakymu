from microbit import *
import music
import random

# display.show(Image.HEART)
# display.scroll("Hello!")


def ghostLocation():
    return random.randint(-10, 10), random.randint(-10, 10)


def move(head):
    return head


X, Y = ghostLocation()
compass.calibrate()
needle = ((15 - compass.heading()) // 30) % 12
display.show(Image.ALL_CLOCKS[needle])

while True:
    if button_a.is_pressed():
        # needle = ((15 - compass.heading()) // 30) % 1
        print(str(needle))
        print()
        display.show("S")
    else:
        needle = ((15 - compass.heading()) // 30) % 12
        display.show(Image.ALL_CLOCKS[needle])
        print()
