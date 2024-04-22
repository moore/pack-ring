# SPDX-FileCopyrightText: 2022 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
from rainbowio import colorwheel
import neopixel

NUMPIXELS = 60  # Update this to match the number of LEDs.
SPEED = 0.05  # Increase to slow down the rainbow. Decrease to speed it up.
BRIGHTNESS = 0.05  # A number between 0.0 and 1.0, where 0.0 is off, and 1.0 is max.
PIN = board.A3  # This is the default pin on the 5x5 NeoPixel Grid BFF.
HUERANGE = 96

#pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=neopixel.RGBW)
#pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False)
pixels = neopixel.NeoPixel(PIN, NUMPIXELS, brightness=BRIGHTNESS, auto_write=False, pixel_order=neopixel.GRBW)


def rainbow_cycle(wait):
    for color in range(255):
        for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
            #pixel_index = (pixel * 256 // len(pixels)) + color * 5
            pixel_index = (pixel * HUERANGE // len(pixels)) + color * 3

            #pixels[pixel] = colorwheel(pixel_index & 255)
            #pixels[pixel] = colorwheel(256+((pixel_index % 84)-42))
        
            pixels[pixel] = colorwheel(256+(abs(HUERANGE/2-(pixel_index % HUERANGE)))-HUERANGE/4)

        pixels.show()
        time.sleep(wait)


def test(wait):
    for pixel in range(len(pixels)):  # pylint: disable=consider-using-enumerate
        pixels[pixel] = colorwheel(pixel*(256/(len(pixels))))

    pixels.show()
    time.sleep(wait)

while True:
    print("loop ", NUMPIXELS, " ", BRIGHTNESS)
    rainbow_cycle(SPEED)
    #test(SPEED)
