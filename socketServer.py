import socket
import struct
from random import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostbyname(""), 1234))
s.listen(5)

while 1:
    servost = (random() - 0.5) * 0.3
    servost = str(int(servost * 100))
    clientsocket, address = s.accept()
    clientsocket.send(bytes(servost, "utf-8"))
    print(0)
    clientsocket.close()
