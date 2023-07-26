import socket

host = '127.0.0.1' #server host , 0.0.0.0 for all connect 
port = 9000 
buffsize = 4096

while True: 
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #set up server 
    server.bind((host,port))
    server.listen(1)
    print('waiting for some body talking .....')

    client, addr = server.accept()
    print('conected from : ',addr)

    data = client.recv(buffsize).decode('utf-8')
    print('Data from client:',data)
    client.send('hello world'.encode('utf-8'))
    client.close()