# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

from time import sleep
from adafruit_motor import servo

from pca import get_pca

pca = get_pca()

servo = servo.Servo(pca.channels[6])
while True:
    servo.angle = 0
    sleep(1)
    servo.angle = 180
    sleep(1)

pca.deinit()
