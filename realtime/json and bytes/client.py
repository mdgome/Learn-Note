import socket
import pickle

HOST = "127.0.0.1"
# HOST = socket.gethostname()
PORT = 5051
HEADERSIZE = 30

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

while True:

    full_msg = b''
    new_msg = True

    #while is buffer used 반복문 쓰는것은 버퍼를 이용한다
    while True:
        msg = s.recv(10) # integer is receiver size 숫자는 recievied 사이즈
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recived")
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)

            new_msg = True
            full_msg = b''

    print (full_msg)

