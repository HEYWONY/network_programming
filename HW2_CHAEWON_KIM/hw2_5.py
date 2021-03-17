#for루프 이용해서 리스트 생성

num = []
num2 = []

for i in range(0, 50):
    num.append(i) 
    num2.append(i*i)

print(num) #0~49까지의 수로 구성되는 리스트
print(num2) #0~49까지 수의 제곱으로 구성되는 리스트