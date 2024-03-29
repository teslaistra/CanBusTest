import time
import can
from can2RNET import *


def dec2hex(dec, hexlen):  # convert dec to hex with leading 0s and no '0x'
    h = hex(int(dec))[2:]
    l = len(h)
    if h[l - 1] == "L":
        l -= 1  # strip the 'L' that python int sticks on
    if h[l - 2] == "x":
        h = '0' + hex(int(dec))[1:]
    return ('0' * hexlen + h)[l:l + hexlen]
print(dec2hex(96,16))
bustype = 'socketcan'
channel = 'can0'
import binascii
import array
bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = bus.recv()


cansend(bus, '0061#80010080')
sleep(0.01)

cansend(bus,'C180200#0202')
sleep(0.01)
cansend(bus,'C180201#210101')
sleep(0.01)

cansend(bus,'C180201#010101')

print('send all')