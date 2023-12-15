import random
import sys

gold_coins = 10
# 初始金币为10个
while True:
    pay_confirm = input("您的初始金币为10个,是否充值?\ny/n\n")
    if pay_confirm == "y" or pay_confirm == "Y":
        while True:
            pay_amount = input("请输入充值金额:")
            if pay_amount.isdigit():
                pay_amount = int(pay_amount)
                gold_coins += pay_amount
                print("您已充值%d个金币!您的金币总数为%d!" % (pay_amount, gold_coins))
                break
            else:
                print("请输入正确的数量!")
        break
    elif pay_confirm != "n" or pay_confirm != "N":
        print("请输入正确的字符!")
# 初始充值
while True:
    # 随机两个骰子点数
    while True:
        bet_confirm = input("请下注!\n1-大\n2-小\n")
        if bet_confirm == "1" or bet_confirm == "2":
            while True:
                bet_amount = input("请输入下注金额:")
                if bet_amount.isdigit():
                    if int(bet_amount) > gold_coins:
                        print("下注金额超过金币数!")
                    else:
                        bet_amount = int(bet_amount)
                        break
                else:
                    print("请输入正确的下注金额!")
            # 下注金额流程
            break
        else:
            print("请输入正确的字符!")
    # 下注流程
    dice_point=random.choice
    dice_point_1 = random.randint(1, 6)
    dice_point_2 = random.randint(1, 6)
    if (bet_confirm == "1" and dice_point_1 + dice_point_2 > 6) or (
        bet_confirm == "2" and dice_point_1 + dice_point_2 < 7
    ):
        gold_coins += bet_amount
        print(
            "骰子1点数为%d,骰子2点数为%d,总点数为%d"
            % (dice_point_1, dice_point_2, (dice_point_1 + dice_point_2))
        )
        print("恭喜你!你赢得了%d个金币!,你现在有%d个金币" % (bet_amount, gold_coins))
    else:
        gold_coins -= bet_amount
        print(
            "骰子1点数为%d,骰子2点数为%d,总点数为%d"
            % (dice_point_1, dice_point_2, (dice_point_1 + dice_point_2))
        )
        print("很不幸!你失去了%d个金币!,你现在有%d个金币" % (bet_amount, gold_coins))
    # 游戏流程
    while True:
        next_game_confirm = input("是否继续游戏?\ny/n\n")
        if next_game_confirm == "n" or next_game_confirm == "N":
            print("您的剩余金币为%d,欢迎下次再来!" % gold_coins)
            sys.exit(0)
        elif next_game_confirm == "y" or next_game_confirm == "Y":
            break
        else:
            print("请输入正确的字符!")
    # 是否继续游戏
    if gold_coins == 0:
        while True:
            pay_amount = input("您的金币已不足,请输入充值金额或输入q退出\n")
            if pay_amount == "q" or pay_amount == "Q":
                sys.exit(0)
            elif pay_amount.isdigit():
                pay_amount = int(pay_amount)
                gold_coins += pay_amount
                print("您已充值%d个金币!您的金币总数为%d!" % (pay_amount, gold_coins))
                break
            else:
                print("请输入正确的字符!")
    # 金币不足启动充值流程