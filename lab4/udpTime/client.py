import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# get local machine name
host = socket.gethostname()
port = 9991

# Receive no more than 1024 bytes
msg = "Send me the time"
s.sendto(msg.encode(), (host, port))
tm, addr = s.recvfrom(1024)
print('Current time from Sever :', tm.decode())
s.close()

