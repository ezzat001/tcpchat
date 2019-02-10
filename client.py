
import socket,select,sys,time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '192.168.1.3'
host = raw_input("Enter your host ip : ")
name = raw_input("Enter your name : ")
print("")
server.connect((host,4444))
def send():
    server.send(("<%s> %s"%(name,message)).encode())
while True: 

	sockets_list = [sys.stdin, server] 

	read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 

	for socks in read_sockets: 
		if socks == server: 
			message = socks.recv(2048) 
			print(message.decode())
		else: 
			message = sys.stdin.readline() 
			send()

			#sys.stdout.write(message)
			sys.stdout.flush() 
server.close() 
