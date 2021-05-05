import socket
import time
import pickle


HOST = "127.0.0.1"
# HOST = socket.gethostname()
PORT = 5051
HEADERSIZE = 30

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    connection, address = s.accept()    
    print(f"Connection from {address} has been established!")

    d = {1:"hey", 2:"there"}
    msg = pickle.dumps(d)

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg
    connection.send(msg)
