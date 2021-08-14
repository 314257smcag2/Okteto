import datetime
import time
import socket
import urllib.request
import _thread


def alive():
    while 1:
        time.sleep(100)
        try:
            print(urllib.request.urlopen("https://app-wwkiyyx.cloud.okteto.net").read().decode('utf-8'))
        except Exception as ex:
            print(datetime.datetime.now(), ex)
        time.sleep(100)
        try:
            print(urllib.request.urlopen("https://app-a-wwkiyyx.cloud.okteto.net").read().decode('utf-8'))
        except Exception as ex:
            print(datetime.datetime.now(), ex)
        time.sleep(100)
        try:
            print(urllib.request.urlopen("https://app-b-wwkiyyx.cloud.okteto.net").read().decode('utf-8'))
        except Exception as ex:
            print(datetime.datetime.now(), ex)
        time.sleep(100)
        try:
            print(urllib.request.urlopen("https://app-c-wwkiyyx.cloud.okteto.net").read().decode('utf-8'))
        except Exception as ex:
            print(datetime.datetime.now(), ex)
        time.sleep(100)
        try:
            print(urllib.request.urlopen("https://app-d-wwkiyyx.cloud.okteto.net").read().decode('utf-8'))
        except Exception as ex:
            print(datetime.datetime.now(), ex)
        time.sleep(100)


def client(clientsocket, addr):
    try:
        data = clientsocket.recv(10240).decode('utf-8')
        print(datetime.datetime.now(), addr, data)
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_body = "<h1>hello</h1>"
        response = response_start_line + "\r\n" + response_body
        clientsocket.send(bytes(response, "utf-8"))
        clientsocket.close()
    except Exception as ex:
        print(datetime.datetime.now(), addr, ex)


print(datetime.datetime.now(), "   start")
_thread.start_new_thread(alive, ())
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('0.0.0.0', 8989))
serversocket.listen(100)
print(datetime.datetime.now(), "   0.0.0.0:8989")
while 1:
    clientsocket, addr = serversocket.accept()
    print(datetime.datetime.now(), addr)
    _thread.start_new_thread(client, (clientsocket, addr))
    time.sleep(1)
print(datetime.datetime.now(), "   exit")



