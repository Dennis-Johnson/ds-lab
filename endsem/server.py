import socket

HOST = '127.0.0.1'
PORT = 9991

# TCP Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print("\nWaiting for Incoming connections...\n")

conn, addr = s.accept()
print("Received connection from ", addr[0])

# Receive the number and decode value
num_ = conn.recv(1024)
num_ = num_.decode()
print(num_, " received from client.\n")

# Reverse the number
rev_num = str(num_)[::-1]
print("Sending reversed number {}".format(rev_num))

# Send reversed number to client
conn.send(rev_num.encode())

s.close()
print("Done. Shutting down.")
