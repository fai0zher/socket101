import socket
import random

host = '127.0.0.1' # same ip for test 
port = 9000 
buffsize = 4096 

teams = ['Fais','Hannan','Ilyas','Sulma']

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.connect((host,port))

select = random.choice(teams) 
server.send(select.encode('utf-8'))

data_sever = server.recv(buffsize).decode('utf-8')
print('Data for server:', data_sever)
server.close()

