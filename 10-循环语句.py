"""
for

while
"""

import random


total = 0
number1 = 0
while True:
    price = random.randint(1, 10000) / 100
    print("当前商品价格为:%.2f" % (price))
    number = int(input("输入购买数量"))
    total += number * price
    number1 += number
    answer = input("当前已购买%d件商品,商品总价为:%.2f,按q退出" % (number1, total))
    if answer == "q":
        break

print("共%d件商品,商品总价为:%.2f" % (number1, total))
