import board
import neopixel
import random
import time

# Variables for NeoPixel function
pin_output_to_pixel_ring = board.D0  # data in attacked to Gemma pin D0
number_of_pixels = 16
# bpp is bits per pixel.
strip = neopixel.NeoPixel(pin_output_to_pixel_ring, number_of_pixels, brightness=0.02, auto_write=False, bpp=4)

def randomize_all():
    print("randomizing underway")
    for i in range(number_of_pixels):
        strip[i] = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            0,
        )
    strip.show()

def pause_before_reset():
    time.sleep(3)
    randomize_all()

def make_primary():
    print(strip)
    for i in range(number_of_pixels):        
        # print(strip[i])
        # Case pixel already prime
        if strip[i][3] == 1:
            continue
        # Case none are 0, decrement smallest
        elif strip[i][0] and strip[i][1] and strip[i][2] != 0:
            if strip[i][0] < strip[i][1] and strip[i][0] < strip[i][2]:
                strip[i] = (strip[i][0] - 1, strip[i][1], strip[i][2], 0)
                strip.show()
            elif strip[i][1] < strip[i][0] and strip[i][1] < strip[i][2]:
                strip[i] = (strip[i][0], strip[i][1] - 1, strip[i][2], 0)
                strip.show()
            elif strip[i][2] < strip[i][0] and strip[i][2] < strip[i][1]:
                strip[i] = (strip[i][0], strip[i][1], strip[i][2] - 1, 0)
                strip.show()
        # Case 2 is 0, decrement smallest non-zero
        elif strip[i][0] != 0 and strip[i][1] != 0:
            if strip[i][0] < strip[i][1]:
                strip[i] = (strip[i][0] - 1, strip[i][1], strip[i][2], 0)
                strip.show()
            else:
                strip[i] = (strip[i][0], strip[i][1] - 1, strip[i][2], 0)
                strip.show()
        # Case 1 is 0, decrement smallest non-zero
        elif strip[i][0] != 0 and strip[i][2] != 0:
            if strip[i][0] < strip[i][2]:
                strip[i] = (strip[i][0] - 1, strip[i][1], strip[i][2], 0)
                strip.show()
            else:
                strip[i] = (strip[i][0], strip[i][1], strip[i][2] - 1, 0)
                strip.show()
        # Case 0 is 0, decrement smallest non-zero
        elif strip[i][1] != 0 and strip[i][2] != 0:
            if strip[i][1] < strip[i][2]:
                strip[i] = (strip[i][0], strip[i][1] - 1, strip[i][2], 0)
                strip.show()
            else:
                strip[i] = (strip[i][0], strip[i][1], strip[i][2] - 1, 0)
                strip.show()
        # Case 0 is not 255, increment
        elif strip[i][0] != 0 and strip[i][0] < 255:
            strip[i] = (strip[i][0] + 1, strip[i][1], strip[i][2], 0)
            strip.show()
        # Case 1 is not 255, increment
        elif strip[i][1] != 0 and strip[i][1] < 255:
            strip[i] = (strip[i][0], strip[i][1] + 1, strip[i][2], 0)
            strip.show()
        # Case 2 is not 255, increment
        elif strip[i][2] != 0 and strip[i][2] < 255:
            strip[i] = (strip[i][0], strip[i][1], strip[i][2] + 1, 0)
            strip.show()
        # Case pixel done, set last byte to 1 
        else:
            strip[i] = (strip[i][0], strip[i][1], strip[i][2], 1)
            #Check if all done
            pixels_already_prime = 0
            for j in range(number_of_pixels):
                if strip[j][3] == 1:
                    pixels_already_prime += 1
            if pixels_already_prime == number_of_pixels:
                pause_before_reset()
                break

while True:
    make_primary()
    time.sleep(.1)