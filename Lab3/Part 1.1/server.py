import socket
HOST = "127.0.0.1" # Symbolic name meaning all available interfaces
PORT = 50007 # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
while True:
	data, addr = s.recvfrom(1024)
	print("From: ", addr)
	print("Received: ", data.decode("utf-8"))
