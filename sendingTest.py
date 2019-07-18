import time
import can
from can2RNET import *

bustype = 'socketcan'
channel = 'can0'
import binascii
import array
bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = bus.recv()
# print(map(ord, msg.data))
# print(map(ord, msg.arbitration_id))
print(msg.arbitration_id)
# stop = can.Message(arbitration_id=0x0c000000, is_extended_id=False)
#

while 1 == 0:

    msg = bus.recv()
    if (msg.arbitration_id == 33554432):
        print(binascii.hexlify(msg.data))
while 0 == 0:
    msg = bus.recv()
    print(binascii.hexlify(msg.data)[0:2])

    if binascii.hexlify(msg.data)[0:2] == "9c":

        print("now will build another message by my own and send it for 1 sec")
        #msg.data = build_frame("123#63")
        print(binascii.hexlify(msg.data))
        print("sending my own message")
        t = time() + 1
        while t > time():
            sleep(0.01)



            msg1 = can.Message(arbitration_id=33554432, data = array.array('B', [156, 0, 0, 0, 0, 0, 0, 0]), is_extended_id=True)
            if msg.data == msg1.data: print ("true")
            else: print("false")
            print(binascii.hexlify(msg.data))

            print(binascii.hexlify(msg1.data))
            print(type(msg.data))
            print (type(msg1.data))
            bus.send(msg1)
        print("done")
        sleep(5)
        break

# bus.send(stop)
# bus.send(stop)

# bus.send(stop)

str = build_frame("181C0100#105a205b00000000")
