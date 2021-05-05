from socket import *
import os
import time
import sys

BUF_SIZE = 1024
LENGTH = 20

sock1 = socket(AF_INET, SOCK_STREAM)
sock1.bind(('', 7777))

sock2 = socket(AF_INET, SOCK_STREAM)
sock2.bind(('', 8888))

conn, addr = sock1.accept()
conn2, addr2 = sock2.accept()

while True:  
    device = input('Enter a device num: ')

    if device == '1':
        # 만약 1을 입력했다면
        conn.send(device.encode())

        msg = conn.recv(BUF_SIZE)
        if not msg:
           conn.close()
           continue
        else :

    elif device == '2':
       # 만약 2를 입력했다면
        conn2.send(device.encode())

        msg = conn.recv(BUF_SIZE)
        if not msg:
           conn.close()
           continue
        else :
            
    elif device == 'quit':
        print('quit')
        conn.close()
        conn2.close()
        break
    else:
        print('Error')
        conn.close()
        conn2.close()
        continue
    

f.close()
conn.close()