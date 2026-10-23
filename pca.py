import board
from adafruit_pca9685 import PCA9685


def get_pca(frequency = 50):
    i2c = board.I2C()
    pca = PCA9685(i2c)
    pca.frequency = frequency
    return pca
