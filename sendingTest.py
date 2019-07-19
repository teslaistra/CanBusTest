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



global msg1
msg = bus.recv()
msg1 = msg
while 0==0:
    msg = bus.recv()
    if (msg.arbitration_id == 33554432):
        while 0==0:
            msg = bus.recv()
            print ("looking")
            if binascii.hexlify(msg.data)[0:2] == "9c":
                print ("got!")
                msg1 = msg
                print("err")
                errmsg = can.Message(arbitration_id=int('0c000000', 16))
                bus.send(errmsg)
                sleep(3)

                print("msg sending")
                time1 = time() + 1
                while time1 > time():
                    sleep(0.005)
                    bus.send(msg)
