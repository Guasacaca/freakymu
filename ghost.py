from microbit import *
import music
import random
import math


# display.show(Image.HEART)
# display.scroll("Hello!")
def ghostLocation():
    return random.randint(-10, 10), random.randint(-10, 10)


right = 3
down = 6
left = 9
top = 0
hintsStarting = 5
steps = 0
ghostX, ghostY = ghostLocation()
X, Y = 0, 0


def isCatched(X, Y, ghostX, ghostY):
    return X == ghostX and Y == ghostY


def hint(steps):
    if(steps > hintsStarting):
        xdiff = X - ghostX
        ydiff = Y - ghostY
        if (ydiff > 0):
            display.show(Image.ARROW_S)
        elif (ydiff < 0):
            display.show(Image.ARROW_N)
        sleep(2000)
        if (xdiff < 0):
            display.show(Image.ARROW_W)
        elif (xdiff > 0):
            display.show(Image.ARROW_E)
        sleep(2000)
        return 0
    else:
        return steps


def move(direction, X, Y):
    if(direction == top):
        display.show(Image.ARROW_N)
        return X, Y+1
    elif(direction == down):
        display.show(Image.ARROW_S)
        return X, Y-1
    elif(direction == right):
        display.show(Image.ARROW_E)
        return X-1, Y
    elif(direction == left):
        display.show(Image.ARROW_W)
        return X+1, Y
    else:
        display.show(Image.ANGRY)
        return X, Y


gameOn = True
print("GX= "+str(ghostX))
print("GY= "+str(ghostY))
compass.calibrate()
display.scroll("Find the ghost")
needle = ((15 - compass.heading()) // 30) % 12
music.play(music.JUMP_UP)
display.show(Image.ALL_CLOCKS[needle])

while gameOn:
    needle = ((15 - compass.heading()) // 30) % 12
    display.show(Image.ALL_CLOCKS[needle])
    if button_a.was_pressed():
        steps = steps+1
        X, Y = move(needle, X, Y)
        print()
        print("X= "+str(X))
        print("Y= "+str(Y))
        display.show("S")
        if(isCatched(X, Y, ghostX, ghostY)):
            display.show(Image.GHOST)
            music.play(music.DADADADUM)
            gameOn = False
    if button_b.was_pressed():
        steps = hint(steps)
