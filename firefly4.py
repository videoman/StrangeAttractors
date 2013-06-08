#!/usr/bin/python
import strip
import random, time
import threading
import Image
import os

random.seed(time.time())

thresh = 100  # charge threshold
charge = 1    # charging rate
sync = 5     # boost given to neighbors
rate = 200     # frames per sec
flashthresh = 150
reset = 180
bright = 15
color = (.5, 1, 0)
fac = 255.0 / bright

d = strip.display()
width = d.width
height = d.height

# build emptyarrays
screen = []
state = []
nstate = []
for y in range(height):
    screen.append([0] * width)
    state.append([0] * width)
    nstate.append([0] * width)

def lit(y, x):
    if 0 <= x < width and 0 <= y < height:
        return screen[y][x] == bright
    return 0

def getimage():
    os.system("raspistill -t 0 -w 128 -h 96 -o /dev/shm/image.jpg")
    i = Image.open("/dev/shm/image.jpg", "r")
    i = i.resize((26, 16),Image.BICUBIC)
    d = i.load()
    return d

cam = camold = getimage()

def camerathread():
    global cam, camold
    while 1:
        new = getimage()
        camold, cam = cam, new

t = threading.Thread(None, camerathread)
t.start()

lastreset = 0

while 1:
    if time.time() - lastreset > reset:
        print "reset"
        d.setall(255, 0, 0)
        d.update()
        time.sleep(.3)
        # set all fireflies to a random state
        for x in range(width):
            for y in range(height):
                nstate[y][x] = random.randint(0, thresh)
        lastreset = time.time()

    # move state forward
    for x in range(width):
        for y in range(height):
            state[y][x] = nstate[y][x]

    # update state
    for x in range(width):
        for y in range(height):
            # fully charged?
            if state[y][x] > thresh:
                # flash on screen
                screen[y][x] = bright

                # lose all charge
                nstate[y][x] = 0
            else:
                # charge up
                nstate[y][x] += charge
                # blank/fade
                if screen[y][x] > 0:
                    screen[y][x] -= 1

    # check neighbors
    for x in range(width):
        for y in range(height):
            if not lit(y, x) and state[y][x] > thresh * .8:
                on = (lit(y-1, x-1) +
                      lit(y-1, x) +
                      lit(y-1, x+1) +
                      lit(y, x-1) +
                      lit(y, x+1) +
                      lit(y+1, x-1) +
                      lit(y+1, x) +
                      lit(y+1, x+1))
                if on:
                    nstate[y][x] += on * sync

    # draw screen
    for y in range(height):
        for x in range(width):
            c = cam[25-x, y]
            o = camold[25-x, y]
            if o[1] < flashthresh and c[1] > flashthresh:
                r,g,b = 128, 0, 255
                nstate[y][x] = thresh
            else:
                r = g = b = 0
            l = screen[y][x]
            d.set2d(x, y,
                    r + color[0] * l * fac,
                    g + color[1] * l * fac,
                    b + color[2] * l * fac)
    d.update()

    time.sleep(1.0/rate)
