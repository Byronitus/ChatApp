import threading
import socket


connection =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.3.227", 445))

message = input("Message : ")
connection.send(message.encode())

initial = connection.recv(1024)
print(initial)

while True:
    message = input("Message : ")
    connection.send(message.encode() + "\n".encode())
    connection.send("Message : ".encode())
    recv = connection.recv(1024)
    print(str(recv))

connection.close()