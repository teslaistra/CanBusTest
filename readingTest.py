import time
import can
from can2RNET import *

import threading
bustype = 'socketcan'
channel = 'can0'

new_messages = {}
drive_messages = {
    '33554432': 'drive control'
}

message_names = {
'1c0c0100': 'JSMrx battery power level in % Xx = 0x00 - 0x64 -p',
 '14300100': 'PMtx drive motor current -p',
 '03c30f0f': 'JSMtx device heartbeat -p',
 '0c140200': 'smth system JSM 1',
 '02000000': 'JSM frame - drive control ',
 '1c300104': 'PMtx distance counter',
 '0000000e': 'serial number',
 '0c140100': 'smth system JSM 2',
}

import binascii
import array
bus = can.interface.Bus(channel=channel, bustype=bustype)


def dec2hex(dec, hexlen):  # convert dec to hex with leading 0s and no '0x'
    h = hex(int(dec))[2:]
    l = len(h)
    if h[l - 1] == "L":
        l -= 1  # strip the 'L' that python int sticks on
    if h[l - 2] == "x":
        h = '0' + hex(int(dec))[1:]
    return ('0' * hexlen + h)[l:l + hexlen]

def dict(msg):
    global message_names
    a = message_names.get(str(dec2hex(msg.arbitration_id, 8)))
    if a != None:
        f = 3
        print('recieved : ')
                #print(message_names[str(dec2hex(msg.arbitration_id, 8))])
                #print('with data: ')
                #print(binascii.hexlify(msg.data))
                #print(' ')
    else:
        print('Adding')
        d1 = {str(dec2hex(msg.arbitration_id,8)) : 'new'}
        print(d1)
        print(' ')
        new_messages.update(d1)







if __name__ == "__main__":
    time1 = time() + 20
    while time() < time1:
        msg= bus.recv()
        dict(msg)
    print(new_messages)