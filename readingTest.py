import time
import can
from can2RNET import *

bustype = 'socketcan'
channel = 'can0'
import binascii
import array
bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = bus.recv()
global running
running = True
def print_thread(bus):
    global running
    global message_names
    print(running)

    while running:
        msg = bus.recv()
        print('alive')
        if message_names[str(msg.arbitration_id)] != None:
            print('recieved: ')
            print(message_names[str(msg.arbitration_id)])
            print(' ')
        else:
            d1 = {str(msg.arbitration_id) : 'new'}
            message_names.update(d1)



message_names = {
    '472908036' : 'distance counter',
    '470548736': 'battery counter',
    '63115023':'device heartbeat',
    '338690304': 'PMtx drive motor current',
    '202637824': 'PMtx heartbeart(??)',
    '202637568': 'PMtx heartbeart(??)',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',

}

running = True

sendjoyframethread = threading.Thread(target=print_thread, args=(bus))
sendjoyframethread.start()
time1 = time() + 10
while time() < time1:
    global running
    running = True
running = False
print(message_names)