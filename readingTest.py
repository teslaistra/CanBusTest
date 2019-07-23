import time
import can
from can2RNET import *

bustype = 'socketcan'
channel = 'can0'
import binascii
import array
bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = bus.recv()

def print_thread(dict, bus):
    global running
    while running == True:
        msg = bus.recv()
        if dict[str(msg.arbitration_id)] != None:
            print('recieved: ')
            print(dict[str(msg.arbitration_id)])
            print(' ')
        else:
            d1 = {str(msg.arbitration_id) : 'new'}
            dict.update(d1)



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

global running
running = True

sendjoyframethread = threading.Thread(target=print_thread,args=(bus,message_names))
sendjoyframethread.start()
time1 = time()
while time < time1:
    global running
    running = True
running = False