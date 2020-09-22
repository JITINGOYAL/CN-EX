from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import thread
import time
import datetime

host = '0.0.0.0'       ### add server IP in place of 0.0.0.0
port = 1234
buf = 1024

addr = (host, port)

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serversocket.bind(addr)
serversocket.listen(10)

clients = [serversocket]

def handler(clientsocket, clientaddr):
    print "Accepted connection from: ", clientaddr
    while True:
        data = clientsocket.recv(1024)
        print "_" + data + "_"
        if data == "bye\n" or not data:
            break

   
        elif data == "client1\n":
            clientsocket.send("sending to client1 from server\n")

        elif "client2" in data:
            clientsocket.send("sending to client2 from server\n")

        else:
            clientsocket.send("ECHO: " + data + '\n')

    clients.remove(clientsocket)
    clientsocket.close()

def push():
    while True:
        for i in clients:
            if i is not serversocket: # neposilat sam sobe
                i.send("Curent date and time: " + str(datetime.datetime.now()) + '\n')
        time.sleep(10) # [s]


thread.start_new_thread(push, ())

while True:
    try:
        print "Server is listening for connections\n"
        clientsocket, clientaddr = serversocket.accept()
        clients.append(clientsocket)
        thread.start_new_thread(handler, (clientsocket, clientaddr))
    except KeyboardInterrupt:
        print "Closing server socket..."
        serversocket.close()