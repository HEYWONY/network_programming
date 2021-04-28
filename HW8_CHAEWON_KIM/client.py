from socket import *

BUFF_SIZE = 1024
port = 3333

sock = socket(AF_INET, SOCK_DGRAM) 

print('메시지를 입력하세요. quit를 누르면 종료됩니다.')
print('send mboxID 또는 receive mboxID를 앞에 붙이세요.')

while True:
    msg = input('->')
    sock.sendto(msg.encode(), ('localhost', port))
    
    if msg == 'quit':
        break

    data, addr = sock.recvfrom(BUFF_SIZE)
    print('<-', data.decode())

sock.close()