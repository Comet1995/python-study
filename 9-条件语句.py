import random

ran = random.randint(1, 10)
print(ran)
cai = input("请输入你猜的数:")
if int(cai) == ran:
    print("正确")
else:
    print("错误")
