import time
import can
from can2RNET import *

bustype = 'socketcan'
channel = 'can0'
import binascii
import array
bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = bus.recv()

cansend(bus, '0060#40000000')
sleep(0.01)
cansend(bus, '0061#60000000')
cansend(bus,'181C0000#0260000000000000')