#최대 공약수 구하는 프로그램

a = int(input('a: '))
b = int(input('b: '))

while(b != 0):
    if a < b:
        a, b = b, a
    (a, b) = (b, (a % b))
    
print(a)
16