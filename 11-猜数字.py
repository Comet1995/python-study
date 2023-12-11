import random


answer = random.randint(1, 100)
guess = 0
while guess != answer:
    guess = int(input("请输入你想猜的数:"))
    if guess < answer:
        print("你猜的数字小了")
    elif guess > answer:
        print("你猜的数字大了")
print("恭喜你!猜对了!")
