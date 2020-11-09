from websocket import create_connection
import sys


arguments = sys.argv

if(len(arguments) != 4):
	raise Exception("Wrong number of arguments")

SERVER = sys.argv[1]
PORT = sys.argv[2]
COMMAND = sys.argv[3]
ws = create_connection("ws://" + SERVER + ":" + PORT)

ws.send(COMMAND)

while True:
	try:
		received = ws.recv()
		print(received.decode(),flush=True)
	except:
		break;

ws.close()

		