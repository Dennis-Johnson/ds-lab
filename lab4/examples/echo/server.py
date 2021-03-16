import socket 

HOST = '127.0.0.1'
PORT = 2053

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()

	conn, addr = s.accept()
	
	with conn:
		print(f"Connected by {addr}")
		while True:
			data = conn.recv(1024)
			if data: 
				print(f"Client sent {data.decode()}")
			
			resp = input("Enter a response to the client: ")
			if not data:
				break
			
			conn.sendall(resp.encode())
	conn.close()
