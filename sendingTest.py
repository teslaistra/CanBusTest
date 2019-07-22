import time
import can
from can2RNET import *

bustype = 'socketcan'
channel = 'can0'
import binascii
import array
bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = bus.recv()

def induce_JSM_error(cansocket):
    for i in range(0, 3):
        cansend(cansocket, '0c000000#')
list =['33554432','472908036','470548736', '63115023', '338690304','202637824','202637568','14']
while 0==0:
    msg = bus.recv()
    if str(msg.arbitration_id) not in list:
        print()
        print(str(msg.arbitration_id))
        print(binascii.hexlify(msg.data))
