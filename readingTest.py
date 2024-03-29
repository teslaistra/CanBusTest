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
 '181c0000': 'song',
 '0c180201': 'seen after change mode to angle',
 '00000062': 'seen after change mode to angle',
 '00000060': 'seen after change mode to angle',
 '00000061': 'seen after change mode to angle',
 '0c180200': 'seen after change mode to angle',
 '0c180101': 'seen after change mode to drive',
 '0c180100': 'seen after change mode to drive',
 '0c000003': 'Blinking button(on the left of panel)',
 '181c0200': 'song',
 '1c240001': 'Device is ready. UI is active.',
 '0c000200': 'unknown',
 '0c000004': 'Lightning Button',
 '0c040000': 'horn on',
 '0c040001': 'horn off',
 '0c000002': 'right turn button',
 '0c000001': 'left turn button',
 '00000051': 'seen when speed changing',
 '00000050': 'seen when speed changing',
 '14300101': 'PMtx angle/height motor current',
 '00000000': 'seen at power off',
 '00000002': 'seen at power off',
 '0000000c': 'used by JSM to check for canbus connection',
 '00000004': 'seen at power off'

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
        print('recieved : ')
        #print(message_names[str(dec2hex(msg.arbitration_id, 8))])
        #print('with data: ')
        #print(binascii.hexlify(msg.data))
        #print(' ')
    else:
        print('Adding')
        d1 = {str(dec2hex(msg.arbitration_id,8)) : 'new'}
        print(d1)
        print(binascii.hexlify(msg.data))

        print(' ')
        new_messages.update(d1)







if __name__ == "__main__":
    time1 = time() + 10
    while time() < time1:
        msg= bus.recv()
        dict(msg)
    print(new_messages)