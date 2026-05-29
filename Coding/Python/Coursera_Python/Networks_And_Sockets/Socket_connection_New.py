import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
print(cmd) ###### encoding format request will print mean string to byte format.
print(type(cmd)) ###### this will print the type of cmd variable which is bytes because we have encoded the string to bytes format.
mysock.send(cmd)
while True:
    data = mysock.recv(512) 
    if (len(data) < 1 ):
        break
    print(data.decode())
    print(type(data)) ###### this will print the type of data variable which is bytes because we have received the data in bytes format from the server.
mysock.close()
