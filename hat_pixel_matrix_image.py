#!/usr/bin/env python

from sense_hat import SenseHat

sense = SenseHat()
r = (255, 0, 0)
b = (0, 0, 255)
w = (255, 255, 255)
speed = 0.05
message = "Hello World!"
pixels = [
    b,b,b,b,r,r,r,r
    b,b,b,b,w,w,w,w
    b,b,b,b,r,r,r,r
    b,b,b,b,w,w,w,w
    r,r,r,r,r,r,r,r
    w,w,w,w,w,w,w,w
    r,r,r,r,r,r,r,r
    w,w,w,w,w,w,w,w
    r,r,r,r,r,r,r,r
sense.show_message(message, speed, text_colour=yellow, back_colour=blue)

sense.clear()






