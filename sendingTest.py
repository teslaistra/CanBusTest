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

while 0==0:
    msg = bus.recv()
    #print(binascii.hexlify(msg.data)[0:2])

    if binascii.hexlify(msg.data)[0:2] == "9c":
        print(binascii.hexlify(msg.data)[0:2])
        sleep(1)
        break
time1 = time() +3
while time1 > time():
    print(123)
    sleep(0.01)
    bus.send(msg)