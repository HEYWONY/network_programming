from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break

        formula = data.decode()
        n_list = formula.split(' ')

        try:
            if n_list[1] == '+':
                result = int(n_list[0]) + int(n_list[2])
            elif n_list[1] == '-':
                result = int(n_list[0]) - int(n_list[2])
            elif n_list[1] == '*':
                result = int(n_list[0]) * int(n_list[2])
            elif n_list[1] == '/':
                result = round(int(n_list[0]) / int(n_list[2]), 1)
        except:
            client.send(b'Try again') 
        else:           
            bytes_str_result = str(result).encode()  
            client.send(bytes_str_result) 
    
    client.close()
s.close()