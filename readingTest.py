import time
import can
from can2RNET import *

import threading
bustype = 'socketcan'
channel = 'can0'

import binascii
import array

bus = can.interface.Bus(channel=channel, bustype=bustype)

def print_thread(bus):
    global t
    global message_names
    global b
    print('sf')
    while t:
        print("aa")
    msg = bus.recv()
    a = message_names.get(str(msg.arbitration_id))
    list = ['472908036', '470548736', '63115023', '338690304', '202637824', '202637568', '14', '33554432']
    if  str(msg.arbitration_id) not in list:
        print('recieved : ')
        print(message_names[str(msg.arbitration_id)])
        print('with data: ')
        print(binascii.hexlify(msg.data))
        print(' ')
    elif a == None:
        print('Adding')
        d1 = {str(msg.arbitration_id) : 'new'}
        print(d1)
        print(' ')
        message_names.update(d1)




message_names = {
    '472908036' : 'distance counter',
    '470548736': 'battery counter',
    '63115023':'device heartbeat',
    '338690304': 'PMtx drive motor current',
    '202637824': 'PMtx heartbeart(??)',
    '202637568': 'PMtx heartbeart(??)',
    '14': 'bitmap of set lamp indicators on JSM',
    '33554432': 'drive control',
    '404488192': 'beep',
    '96': 'joy mode',
    '97': 'smth connected with joy mode 1',
    '202899968': 'seen after mode change - 1',
    '202899969': 'seen after mode change - 2',
    '98': 'smth connected with joy mode 2',
    '': '',
    '': '',
    '': '',
}


if __name__ == "__main__":
    global t
    t = True
    print("dd")
    sendjoyframethread = threading.Thread(target=print_thread,args=bus)
    sendjoyframethread.start()
    print("sd")
