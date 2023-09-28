import socket

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((socket.gethostbyname(""), 1234)) 
    msg = s.recv(1024)
    if len(msg) <= 0:
        continue
    msg = msg.decode("utf-8")
    print(int(msg)/100.0)