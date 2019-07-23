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
    msg = bus.recv()
    a = message_names.get(str(msg.arbitration_id))
    list = ['472908036', '470548736', '63115023', '338690304', '202637824', '202637568', '14', '33554432', '404488192']
    if a != None and  str(msg.arbitration_id) not in list:
        print('recieved : ')
        print(message_names[str(msg.arbitration_id)])
        print('with data: ')
        print(binascii.hexlify(msg.data))

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
    '14': 'bitmap of set lamp indicators on JSM',
    '33554432': 'drive control',
    '404488192': 'beep',
    '96': 'joy mode',
    '97': 'smth connected with joy mode',
    '202899968': 'seen after mode change - 1',
    '202899969': 'seen after mode change - 2',
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
    print_thread(bus)
running = False
print(message_names)