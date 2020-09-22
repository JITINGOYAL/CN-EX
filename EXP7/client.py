import socket

host = 'localhost'
port = 1234
buf = 1024

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

print ("Sending 'client1 to server\\n'")
clientsocket.send('client1\n')
print "REPLY From Server: " + clientsocket.recv(buf)

print "Sending 'client2'"
clientsocket.send('client2')
print "REPLY From server: " + clientsocket.recv(buf)

print "Sending 'abc'"
clientsocket.send('abc')
print "REPLY From Server: " + clientsocket.recv(buf)

print "Sending 'abc'"
clientsocket.send('abc')
print "REPLY From Server: " + clientsocket.recv(buf)


print "Sending 'bye'"
clientsocket.send('bye\n')
print "REPLY From Server: " + clientsocket.recv(buf)

clientsocket.close()

