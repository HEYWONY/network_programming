from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    op = input("수식을 입력하세요. (q를 누르면 종료합니다.) : ")
    if op == 'q':
        break
    s.send(op.encode())

    print('결과 : ', s.recv(1024).decode())

s.close()