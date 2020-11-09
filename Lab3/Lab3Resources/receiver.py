import socket
import sys
import math
import struct 

arguments = sys.argv

if(len(arguments) != 3):
	raise Exception("Wrong number of arguments")


GROUP = sys.argv[1]
PORT = int(sys.argv[2])


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('',int(PORT)))

group = socket.inet_aton(GROUP)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


while True:
  print(sock.recvfrom(1024), flush= True)
