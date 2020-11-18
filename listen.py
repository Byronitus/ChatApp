import socket

listener  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.3.227", 445))
listener.listen(0)

connection, addr = listener.accept()

# print(connection)

# print(listener.accept())

initial_message = connection.recv(1024)
print(initial_message)
while True:
    message = input("Message :")
    connection.send(message.encode())
    reply = connection.recv(1024)
    print(reply)
    
