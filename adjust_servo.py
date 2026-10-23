# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from time import sleep
from adafruit_motor import servo

from pca import get_pca

pca = get_pca()

servo_list = [
    servo.Servo(channel)
    for channel in pca.channels
]

while True:
    try:
        x = input("Input: ")
        if x == "q":
            break

        x = int(x)
        i = x
        if i < 0:
            i = -i
        servo = servo_list[i]
        angle = servo.angle + (5 if 0 < x else -5)
        if 0 <= angle <= 180:
            servo.angle += 5 if 0 < x else -5

    except:
        pass

pca.deinit()
