import socket
port = 8280               
s = socket.socket()  
host=input(str("enter host address"))
s.connect((host,port))
print("connected")
while True:
	file_data=s.recv(600)
	print(file_data)
	
s.close()
