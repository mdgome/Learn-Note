# import json
# import os
# import time

# def tail(stream_file):
#     stream_file.seek(0, os.SEEK_END)

#     while True:
#         if stream_file.closed:
#             raise StopIteration
#         line = stream_file.readline()

#         yield line

# def log_to_db(log_path, db):
#     with open(log_path, "r") as log_file
#         for line in tail(log_file):
#             try:
#                 log_data = json.loads(line)
#             except ValueError:
#                 continue
#             print(log_data["message"])


import socket
import time

HOST = "127.0.0.1"
# HOST = socket.gethostname()
PORT = 5051
HEADERSIZE = 30

# def receive(nb_bytes, conn):
#     received = bytearray()
#     while len(received) < nb_bytes:
#         received += conn.recv(nb_bytes - len(received))

#     return received

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    connection, address = s.accept()    
    print(f"Connection from {address} has been established!")

#   print(f'{len(msg):<10}'+msg) # " '<10' is Header{buffer} size"
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    
    connection.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(1)
        msg = f'The time is! {time.time()}'
        msg = f'{len(msg):<{HEADERSIZE}}' + msg
        connection.send(bytes(msg, "utf-8"))
