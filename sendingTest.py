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
    msg = bus.recv
    if msg.arbitration_id == 33554432 and binascii.hexlify(msg.data)[0:2] == "9c":
        time1 = time() + 1
        while time1 > time:
            bus.send(msg)


msgR = can.Message(arbitration_id =33554432, data = bytearray([0,156]), extended_id = True)
msgL = can.Message(arbitration_id =33554432, data = bytearray([0,100]), extended_id = True)
print("sending L")
time1 = time()+1
while time1 > time:
    bus.send(msgL)
sleep(3)
print("sending R")
while time1 > time:
    bus.send(msgR)