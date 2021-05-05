from socket import *

port = 3333
BUFFSIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))
mboxID = {}

print ('연결되었습니다.')

while True:
    data, addr = sock.recvfrom(BUFFSIZE)

    msg = data.decode()
    a = msg.split()
    message = a[2:]
    message = " ".join(message)

    print(msg)

    if a[0] == 'send': #send일 떄
        if a[1] in mboxID:
            mboxID[a[1]].append(message) #리스트에 요수 요소 추가        
        else:
            mboxID[a[1]] = [message]

        sock.sendto(b'ok', addr)

    elif a[0] == 'receive': #receive일 떄
        if a[1] in mboxID: 
            sock.sendto(mboxID[a[1]][0].encode(), addr)
            
            if len(mboxID[a[1]])==1:
                del mboxID[a[1]]
            elif len(mboxID[a[1]])>1:
                del mboxID[a[1]][0]
            else:
                sock.sendto(b"No messages", addr)
        else:
            sock.sendto(b"No messages", addr)

    elif msg == 'quit': #quit 누르면 종료
        break

sock.close()