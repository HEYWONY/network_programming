import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

sock.send(b'Chaewon Kim') #앞에 b 붙여야 됨
number = sock.recv(1028)
print(int.from_bytes(number, 'big'))

sock.close()