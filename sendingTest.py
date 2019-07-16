import socket, sys, os, struct, array, threading
from time import *
from fcntl import ioctl
from can2RNET import *
cansendtxt = "0C000402#"
out=build_frame(cansendtxt)
print (struct.unpack('B',out[:1]))