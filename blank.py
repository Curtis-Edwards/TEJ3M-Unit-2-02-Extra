# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

blink_time = 1

while True:
    led.value = True
    time.sleep(blink_time)
    led.value = False
    time.sleep(1)
    blink_time = blink_time + 1