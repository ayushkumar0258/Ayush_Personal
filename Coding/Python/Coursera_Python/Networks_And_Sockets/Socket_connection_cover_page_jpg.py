import socket
import os
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org', 80))

cmd = 'GET /cover.jpg HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()

mysock.send(cmd)

count = 0

file = open("cover.jpg", "wb")

while True:
    data = mysock.recv(512)

    if len(data) < 1:
        break

    count += len(data)

    file.write(data)

print("Downloaded bytes:", count)
print("Image downloaded and saved at :",os.getcwd())

file.close()
mysock.close()