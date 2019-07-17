import time
import can
from can2RNET import *
bustype = 'socketcan'
channel = 'can0'

bus = can.interface.Bus(channel=channel, bustype=bustype)
msg = bus.recv()
#print(map(ord, msg.data))
#print(map(ord, msg.arbitration_id))
print(msg.arbitration_id)
#stop = can.Message(arbitration_id=0x0c000000, is_extended_id=False)
#
for msg in bus:
		print(msg.data)
while 0==0:

	msg = bus.recv()
	if(msg.arbitration_id == 33554432):
		print(map(ord,msg.data))

#bus.send(stop)
#bus.send(stop)

#bus.send(stop)

#str = build_frame("181C0100#105a205b00000000")

msg = can.Message(arbitration_id=0x0c040100, is_extended_id=True)
bus.send(msg)
sleep(0.5)
msg = can.Message(arbitration_id=0x0c040101, is_extended_id=True)
bus.send(msg)
sleep(0.5)
msg = can.Message(arbitration_id=0x181c0100,data = build_frame("0x181c0100#2056080010560858"), is_extended_id=True)
bus.send(msg)
msg = can.Message(arbitration_id=0x0c040101, is_extended_id=True)
bus.send(msg)
