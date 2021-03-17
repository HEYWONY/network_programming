#게임 프로그램 작성

from random import randint

money = 50

print("게임을 시작합니다. 0달러 이하로 내려가거나 100달러를 넘기면 게임이 끝납니다.")

while True: 
    if money <= 0:
        print("0달러 아래로 내려갔습니다.")
        break
    elif money >= 100:
        print("100달러를 넘겼습니다.")
        break
    else:
        coin = randint(1,2)
        print("동전 앞면은 1, 뒷면은 2입니다. 1과 2중 하나를 입력해주세요.")
        res = int(input())
        if res == coin:
            print("정답! 9달러 획득")
            money += 9
            print("현재 금액: ", money)
        else:
            print("땡! 10달러 상실")
            money -= 10
            print("현재 금액: ", money)

print("게임이 끝났습니다.")