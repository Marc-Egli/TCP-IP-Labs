import socket
import ssl
import sys

arguments = sys.argv

if(len(arguments) != 3):
	raise Exception("Wrong number of arguments")


CERT = sys.argv[1]
KEY = sys.argv[2]


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('127.0.0.1', 5003))
sock.listen(1)

while True :
	conn, addr = sock.accept()

	ssock = ssl.wrap_socket(conn, server_side=True, certfile=CERT,
                keyfile=KEY)

	request = ssock.recv(1024)
	print(request)
	ssock.send(b"This is PMU data 0")