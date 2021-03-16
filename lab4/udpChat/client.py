import socket

HOST = '127.0.0.1'
PORT = 1621 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

name = input(str("\nEnter your name: "))

print("\nSending to ", HOST, "(", PORT, ")\n")
s.sendto(name.encode(), (HOST, PORT))

s_name, addr = s.recvfrom(1024)
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:
	message, addr = s.recvfrom(1024)
	print(s_name, ":", message)

	message = input(str("Me : "))

	if message == "[e]":
		message = "Left chat room!"
		s.sendto(message.encode(), addr)
		print("\n")
		break

	s.sendto(message.encode(), addr)

