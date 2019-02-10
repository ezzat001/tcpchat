
import socket 
import select 
import sys,os
from thread import *
host = socket.gethostname()

print("Welcome to Ezzat's Chat Server Side\n")
import socket
def ge(): 
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
   try: 
 
      s.connect(('10.255.255.255', 1)) 
      IP = s.getsockname()[0] 
   except: 
      IP = '127.0.0.1' 
   finally: s.close() 
   return IP
print(ge())





server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

	
ipaddr = ge()
IP_address = ipaddr



server.bind((IP_address, 4444)) 

server.listen(100) 
print("Server is up")
print("Server Name : %s\nHost : %s"%(host,ipaddr))

list_of_clients = [] 

def clientthread(conn, addr): 

	conn.send("Welcome to this chatroom!".encode()) 

	while True: 
			try: 
				message = conn.recv(2048) 
				if message: 

					print(message.decode())

					# Calls broadcast function to send message to all 
					message_to_send = "<%s> %s"%("SERVER",message.encode())
					broadcast(message, conn) 

				else: 
					
					remove(conn) 

			except: 
				continue

def broadcast(message, connection): 
	for clients in list_of_clients: 
		if clients!=connection: 
			try: 
				clients.send(message.encode()) 
			except: 
				clients.close() 

				remove(clients) 
def remove(connection): 
	if connection in list_of_clients: 
		list_of_clients.remove(connection) 

while True: 

	conn, addr = server.accept() 
	list_of_clients.append(conn) 

	print(addr[0] + " is on")

	
	start_new_thread(clientthread,(conn,addr))

conn.close() 
server.close() 
