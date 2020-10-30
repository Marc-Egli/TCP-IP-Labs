import socket
import sys
import math

arguments = sys.argv

if(len(arguments) != 4):
	raise Exception("Wrong number of arguments")


SERVER = sys.argv[1]
PORT = sys.argv[2]
COMMAND = sys.argv[3]



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER,int(PORT)))

sock.sendall(COMMAND.encode())

received = 0
MSG_LEN = 18
while True:
	size = MSG_LEN
	if received != 0 :
		size = MSG_LEN + math.floor(math.log10(received))

	print(size)
	data = sock.recv(size).decode()
	if data :
		print(data)
		received += 1
	else :
		break
	

