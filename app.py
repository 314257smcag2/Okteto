import datetime
import time
import socket
print(datetime.datetime.now(), "   start")
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8989))
serversocket.listen(100)
print(datetime.datetime.now(), "   0.0.0.0:8989")
while 1:
    clientsocket,addr = serversocket.accept()
    print(datetime.datetime.now(), addr)
    while 1:
        try:
            data = clientsocket.recv(1024).decode('utf-8')
            print(datetime.datetime.now(),addr,data)
            msg = "hello"
            clientsocket.send(msg.encode('utf-8'))
        except:
            print(datetime.datetime.now(),addr,"exception")
            break
    clientsocket.close()
    print(datetime.datetime.now(), "   close")
    time.sleep(1)
print(datetime.datetime.now(), "   exit")