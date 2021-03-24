import sys

days = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}


#사용자가 월을 입력하면 해당 월에 일수를 출력하라.
month = input('월을 입력하세요: ')
print(days[month])
print()


#알파벳 순서로 모든 월을 출력하라.
print('알파벳 순서로 모든 월 출력하기')
print(sorted(days))
print()


#일수가 31인 월을 모두 출력하라.
print('일수가 31일인 월을 모두 출력하기')
for key, value in days.items():
    if value == 31:
        print(key)
print()

#월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라.
print('월의 일수를 기준으로 오름차순 정렬하기')
for key, value in sorted(days.items(), key=lambda x: x[1]):
    print(key, value)
print()

#사용자가 월을 3자리만 입력하면 월의 일수를 출력하라.(Jan, Feb 등)
month = input("월을 3자리만 입력하세요: ")
for key, value in days.items():
    if month in key:
        print(value)
    