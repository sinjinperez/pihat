#!/usr/bin/env python
import random
from sense_hat import SenseHat
sense = SenseHat()
x = random.randint(0,8)
y = random.randint(0,8)













sense.set_pixel(x, y, (255, 0, 0))
