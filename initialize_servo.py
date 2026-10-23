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
for servo in servo_list:
    servo.angle = 0
for servo in servo_list:
    servo.angle = 180
for servo in servo_list:
    servo.angle = 90

pca.deinit()
