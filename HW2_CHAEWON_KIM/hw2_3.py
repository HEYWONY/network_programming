#나머지 문자열 출력

word = input('Your word: ')

a = word.find('a')

print(word[:a+1])
print(word[a+1:])