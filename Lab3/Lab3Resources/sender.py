import socket
import sys
import math
import struct
from statistics import mean 

arguments = sys.argv

if(len(arguments) != 4):
	raise Exception("Wrong number of arguments")

GROUP = sys.argv[1]
PORT = sys.argv[2]
SCIPER = sys.argv[3]


message = input("Please enter the message you want to multicast : ")

multicast_group = (GROUP, int(PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL,ttl)

sent = sock.sendto((SCIPER + " " + message).encode() , multicast_group)
