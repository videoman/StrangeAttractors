#!/usr/bin/python
import spi 
import random
import math
from time import sleep

debug=1
random.seed()

SLEEPTIME=2

status = spi.openSPI(speed=5000000)
print "SPI configuration = ", status
# print "PY: initialising SPI mode, reading data, reading length . . . \n"

# How many total pixels?
pixels = 425

class display(object):
   def __init__(self, pixels):
      self.pixels = pixels
      self.clear()
   def update(self):
      spi.transferrgb(self.red, self.green, self.blue)
   def set(self, pos, rv, gv, bv):
      '''set pixel at pos to rgb'''
      self.red[pos] = rv
      self.green[pos] = gv
      self.blue[pos] = bv
   def setall(self, rv, gv, bv):
      '''set all pixels to rgb'''
      for pos in xrange(self.pixels):
         self.red[pos] = rv
         self.green[pos] = gv
         self.blue[pos] = bv
   def clear(self):
      '''clear all pixels to black'''
      self.red = [0] * pixels
      self.green = [0] * pixels
      self.blue = [0] * pixels

# How many pixels in the display do we have?
d = display(416)

#This is due to a bug.  
actpixels = 416
time_counter = 0

d.clear()
d.update()

time_counter = []

for p_temp in xrange(actpixels):
  time_counter.append(random.randrange(0,5))

while 1:
# For each pixel in the list, if the current pixels time counter is 5, turn that pixel on.
# This set that pixels time couter to zero.  Otherwise turn that pixel off.
  for temp_pix in xrange(actpixels):
    if(time_counter[temp_pix] >= 5):
       d.set(temp_pix, 0, 255, 0)
       time_counter[temp_pix] = 0
    else:
      d.set(temp_pix, 0, 0, 0)
      temp_pix_r = temp_pix + 1
      if(temp_pix_r < actpixels):
      	# temp_pix_r = 0
        if(time_counter[temp_pix_r] > time_counter[temp_pix] and time_counter[temp_pix_r] != time_counter[temp_pix]):
          time_counter[temp_pix] = time_counter[temp_pix] + 1
       # print( "time counter", temp_pix, time_counter[temp_pix])
      # time_counter[temp_pix] = int(math.fabs((time_counter[temp_pix_r] - time_counter[temp_pix] ) / 2 ))
      #time_counter[temp_pix] = time_counter[temp_pix] + random.randrange(0,5)
       # print( "time counter right", temp_pix_r, time_counter[temp_pix_r])
      #print( "time counter", temp_pix, time_counter[temp_pix])
       # print( "---------" )
     

    #if(debug == 1):
    #  print("Time counter is set to", temp_pix, time_counter[temp_pix])
  for temp_pix in xrange(actpixels):
      time_counter[temp_pix] = time_counter[temp_pix] + 1 
  d.update()
  sleep(1)
