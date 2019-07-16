import time
import can
from can2RNET import *
bustype = 'socketcan'
channel = 'can0'

bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = bus.recv()
#print(map(ord, msg.data))
#print(map(ord, msg.arbitration_id))
print(msg.data)
stop = can.Message(arbitration_id=0x0c000000, is_extended_id=False)

bus.send(stop)
bus.send(stop)

bus.send(stop)

#str = build_frame("181C0100#105a205b00000000")
time.sleep(10)
msg = can.Message(arbitration_id=0x0c040100, is_extended_id=False)
bus.send(msg)