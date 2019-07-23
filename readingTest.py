import time
import can
from can2RNET import *

import threading
bustype = 'socketcan'
channel = 'can0'

import binascii
import array
global bus
bus = can.interface.Bus(channel=channel, bustype=bustype)

def print_thread(bus):
    global running
    while running:
        msg = bus.recv()
        a = message_names.get(str(msg.arbitration_id))

        if a != None:
            print('recieved : ')
            #print(message_names[str(msg.arbitration_id)])
            #print('with data: ')
            #print(binascii.hexlify(msg.data))
            #print(' ')
        else:
            print('Adding')
            d1 = {str(msg.arbitration_id) : 'new'}
            print(d1)
            print(' ')
            message_names.update(d1)


periodic_messages = {
'472908036' : 'distance counter',
    '470548736': 'battery counter',
    '63115023': 'device heartbeat',
    '63115023': 'device heartbeat',
    '338690304': 'PMtx drive motor current',
    '202637824': 'PMtx heartbeart(??)',
    '202637568': 'PMtx heartbeart(??)',
    '14': 'bitmap of set lamp indicators on JSM',
}

controlling_messages = {
    '33554432': 'drive control',
    '404488192': 'beep',
    '96': 'joy mode',
    '97': 'smth connected with joy mode 1',
    '202899968': 'seen after mode change - 1',
    '202899969': 'seen after mode change - 2',
    '98': 'smth connected with joy mode 2',
}

drive_messages = {
    '33554432': 'drive control'
}



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

    '2': 'seen at poweroff',
    '12': 'JSMtx test canbus connection',
    '': '',
    '': '',
    '': '',
    '': '',
    '': '',
}


if __name__ == "__main__":
    global running
    running = True
    global bus
    global  message_names
    read_thread = threading.Thread(target=print_thread, args=(bus,))
    read_thread.start()
    time1 = time() + 20
    while time() < time1:
        running = True
    running = False
    print(message_names)