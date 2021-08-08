# CircuitPython Gemma Gear goggles
# uses two 16 NeoPixel rings (RGBW)
# connected to Gemma M0 powered by LiPo battery

import board
import neopixel
import time
try:
	import urandom as random
except ImportError:
	import random


pixpinRight = board.D0 #Data In attached to Gemma pin D0
numpix = 16
strip = neopixel.NeoPixel(pixpinRight, numpix, bpp=4, brightness=.05,
    auto_write=False)



def cog(pos):
    # Input a value 0 to 255 to get a color value.
    # Note: switch the commented lines below if using RGB vs. RGBW NeoPixles
    if (pos < 8) or (pos > 250):
        return (0, 191, 255, 0) #first color, red: for RGBW NeoPixels
        #return (120, 0, 0) #first color, red: for RGB NeoPixels
    if (pos < 85):
        #return (int(pos * 3), int(255 - (pos*3)), 0)
        return (139, 0, 139, 0) #second color, brass: for RGBW NeoPixels
        #return (125, 35, 0) #second color, brass: for RGB NeoPixels
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3), 0)#: for RGBW NeoPixels
        #return (int(255 - pos*3), 0, int(pos*3))#: for RGB NeoPixels
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3), 0)#: for RGBW NeoPixels
        #return (0, int(pos*3), int(255 - pos*3))#: for RGB NeoPixels

def brass_cycle(wait, patternL, patternR):
    # patterns do different things, try:
    # 1 blink
    # 24 chase w pause
    # 64 chase
    # 96 parial chase
    # 128 half turn
    # 230 quarter turn w blink
    # 256 quarter turn
    for j in range(255):
        for i in range(len(strip)):
            idxL = int ((i * patternL / len(strip)) + j)

            idxR = int ((i * patternR / len(strip)) + j)
            strip[i] = cog(idxR & 230) #sets the second (brass) color
        strip.show()
        
        time.sleep(wait)

while True:
    brass_cycle(0.01, 256, 64)     # brass color cycle with 1ms delay per step
                                    # patternL, patternR
