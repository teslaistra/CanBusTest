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
time1 = time() + 3
while time1 > time():
    msg = bus.recv()
    print(binascii.hexlify(msg.data)[0:2])
while 0==0:
    if binascii.hexlify(msg.data)[0:2] == "9c":
        break
msgL = msg
msgR = msg
msgR = can.Message(data = bytearray([0,156]), extended_id = True)#arbitration_id =33554432,
msgL = can.Message(data = bytearray([0,100]), extended_id = True)
print("sending L")
time1 = time()+1
while time1 > time:
    bus.send(msgL)
sleep(3)
print("sending R")
while time1 > time:
    bus.send(msgR)