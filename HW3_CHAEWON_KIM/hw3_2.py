  
d = [{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, 
    {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, 
    {'name':'Princess', 'phone':'555-3141', 'email':''}, 
    {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

#전화번호가 8로 끝나는 사용자의 이름을 출력하라.
list = []
for i in range(len(d)):
    if d[i]['phone']:
        number = d[i]['phone']
        if number[-1] == '8':
            list.append(d[i]['name'])
print('전화번호가 8로 끝나는 사용자의 이름은: ' , list)

#이메일이 없는 사용자 이름을 출력하라.
list2 = []
for i in range(len(d)):
    if d[i]['email']:
        continue
    else:
        list2.append(d[i]['name'])
print('이메일이 없는 사용자의 이름은: ', list2)

#사용자 이름을 입력하면 전화번호, 이메일을 출력하라. 이름이 없으면 '이름이 없습니다'라는 메시지를 출력하라
name = input("이름을 입력하세요: ")
flag = True
for i in range(len(d)):
    if d[i]['name'] in name:
        print("phone: " + d[i]['phone'])
        print("email: " + d[i]['email'])
        flag = False
if flag == True:
    print("이름이 없습니다.")