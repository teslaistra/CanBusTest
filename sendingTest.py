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
        sleep(5)
        t = time() + 1

        print("error inducing")
        induce_JSM_error(bus)
        while t > time():
            sleep(0.01)
            #a = array.array('B', build_frame("#9c"))

            a = array.array('B', [156,0])
            print(build_frame("#9c"))
            print("arrays be hand")
            print(binascii.hexlify(a))
            b = msg.data
            print("array from msg")
            print(binascii.hexlify(b))
            print ("array from lib")
            c1 = build_frame("#9c00")
            c = array.array('B', c1)
            print(binascii.hexlify(c))
            msg1 = can.Message(arbitration_id=33554432, data=a, is_extended_id=True)
            bus.send(msg1)
            #bus.send(msg)
        print("done")
        sleep(5)
        break

# bus.send(stop)
# bus.send(stop)

# bus.send(stop)

str = build_frame("181C0100#105a205b00000000")
