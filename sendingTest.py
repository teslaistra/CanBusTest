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




msg = bus.recv()

if (msg.arbitration_id == 33554432):
    while 0==0:
        msg = bus.recv()
        print ("looking")
        if binascii.hexlify(msg.data)[0:2] == "9c":
            print ("got!")

            errmsg = can.Message(arbitration_id=int("0c000000",16))
            for i in range(0,3):
                print ()
                bus.send(errmsg)
            sleep(3)
            print ("asd")
            time1 = time() + 2
            while time1 > time():
                sleep(0.005)
                bus.send(msg)