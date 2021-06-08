import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
port = 9991


# Input number to send
number = input("Enter a number to send to the server: ")

# Connection to hostname on the port.
print("\nTrying to connect to ", host, "(", port, ")\n")
s.connect((host, port))
print("Connected...\n")

# Send the number
s.send(number.encode())

# Receive no more than 1024 bytes
returned_num = s.recv(1024)
print('Number returned from server:', returned_num.decode())

s.close()
print("Done. Shutting down.")

