import os
import Image
import strip

d = strip.display()

while 1:
    os.system("raspistill -t 0 -w 128 -h 96 -o /dev/shm/image.jpg")
    i = Image.open("/dev/shm/image.jpg", "r").convert("LA")
    i = i.resize((26, 16),Image.BICUBIC)

    for x in xrange(d.width):
        for y in xrange(d.height):
            p = i.getpixel((x, y))[0]
            #if p > 100:
            #    p = 255
            #else:
            #    p = 0
            d.set2d(25-x, y, p, p, p)
    d.update()
