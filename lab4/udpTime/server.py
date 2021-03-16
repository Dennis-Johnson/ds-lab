import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()
port = 9991

# bind to the port
serversocket.bind((host, port))

while True:
	data, addr = serversocket.recvfrom(1024)
	
	if not data:
		continue

	print(data.decode(), addr)
	currentTime = time.ctime(time.time()) + "\r\n"
	serversocket.sendto(currentTime.encode('ascii'), addr)
serversocket.close()
