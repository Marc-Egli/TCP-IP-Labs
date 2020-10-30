import socket
import sys
import math
from statistics import mean 

arguments = sys.argv

if(len(arguments) != 3):
	raise Exception("Wrong number of arguments")

TIMEOUT = 1
SERVER = sys.argv[1]
PORT = sys.argv[2]
RESET_CMD = "RESET:20"


s_4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)

s_4.settimeout(0.1)
s_6.settimeout(0.1)


while True :
	s_4.sendto(RESET_CMD.encode(), (SERVER,int(PORT)))

	try:
		data_4, adrr = s_4.recvfrom(1024)
		if data_4 :
			print(data_4)
			print("Runs on IPv4")
			break
	except Exception:
		print("Nothing on IPv4")


	s_6.sendto(RESET_CMD.encode(), (SERVER,int(PORT)))

	try:
		data_6, adrr = s_6.recvfrom(1024)
		if data_6 :
			print(data_6)
			print("Runs on IPv6")
			break
	except Exception:
		print("Nothing on IPv6")






s_4.close()
s_6.close()
