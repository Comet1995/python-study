import random
import time

num_choose = input(
    """
位数选择：

1 -- 一位数
2 -- 两位数
3 -- 三位数
4 -- 四位数
5 -- 五位数
"""
)
while num_choose not in ["1", "2", "3", "4", "5"]:
    print("请输入正确的字符！")
    num_choose = input()
num_choose=int(num_choose)
loop_choose = input(
    """
进行轮数：
"""
)
while loop_choose.isdigit() is False:
    print("请输入正确的字符！")
    loop_choose = input()
loop_choose=int(loop_choose)
correct = 0
wrong = 0
q_num = 1
wrong_list = []
time_1 = time.time()
while q_num <= loop_choose:
    num_1 = random.randint(10 ** (num_choose - 1), 10 ** num_choose)
    num_2 = random.randint(10 ** (num_choose - 1), 10 ** num_choose)
    operator = random.randint(1, 2)
    if operator == 1:
        result = input("%d. %d+%d=" % (q_num, num_1, num_2))
        if int(result) == num_1 + num_2:
            correct += 1
        else:
            wrong += 1
            wrong_list.append(q_num)
        q_num += 1
    elif operator == 2:
        result = input("%d. %d-%d=" % (q_num, num_1, num_2))
        if int(result) == num_1 - num_2:
            correct += 1
        else:
            wrong += 1
            wrong_list.append(q_num)
        q_num += 1
time_2 = time.time()
print(
    """
练习结束，正确%d道，错误%d道，正确率百分之%.2f，用时%.2fS，平均每题用时%.2fS。
"""
    % (
        correct,
        wrong,
        (correct / int(loop_choose) * 100),
        (time_2 - time_1),
        ((time_2 - time_1) / int(loop_choose)),
    )
)
if wrong > 0:
    print("错题号为：", wrong_list)
