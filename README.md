# Robot Arm Operation Program with Raspberry Pi referencing uroa.jp

##

## Setup

### Enabling I2C on Raspberry Pi

Please search.

### Installing software

```bash
sudo apt update
sudo apt install libcamera-apps libcamera-dev v4l-utils
sudo apt install qtbase5-dev
sudo apt install libxkbcommon-x11-dev
```

### Installing UV and Python Packages

https://docs.astral.sh/uv/getting-started/installation/

```bash
uv venv --python /usr/bin/python3 --system-site-packages
uv pip install adafruit-circuitpython-dht
uv add opencv-contrib-python pysimplegui pyserial scikit-learn matplotlib pandas requests tqdm openvino
```

## If needed

```bash
# Change name resolution server
nameserver 8.8.8.8 >> /etc/resolv.conf
nameserver 8.8.4.4 >> /etc/resolv.conf
```

## Grateful References

https://uroa.jp/arm/

https://pydevtools.com/handbook/how-to/how-to-use-picamera2-and-gpio-with-uv-on-raspberry-pi/
