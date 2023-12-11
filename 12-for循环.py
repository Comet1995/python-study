import random

number_of_gold_coins = 10
payment_confirmation = input("您的初始金币为10个,是否充值?\ny/n\n")
if payment_confirmation == "y" or payment_confirmation == "Y":
    payment_amount = int(input("请输入充值金额:"))
    number_of_gold_coins += payment_amount
    print("您已充值%d个金币!您的金币总数为%d!" % (payment_amount, number_of_gold_coins))
while True:
    if number_of_gold_coins == 0:
        payment_amount = input("请输入充值金额或输入q退出\n")
        if payment_amount == "q" or payment_amount == "Q":
            break
        else:
            number_of_gold_coins += int(payment_amount)
            print("您已充值%d个金币!您的金币总数为%d!" % (payment_amount, number_of_gold_coins))
    dice_point_number_1 = random.randint(1, 6)
    dice_point_number_2 = random.randint(1, 6)
    betting = input("请下注!\n1-大\n2-小\n")
    bet_amount = int(input("请输入下注金额:"))
    if bet_amount > number_of_gold_coins:
        print("下注金额超过金币数!")
        continue
    elif (betting == "1" and dice_point_number_1 + dice_point_number_2 > 6) or (
        betting == "2" and dice_point_number_1 + dice_point_number_2 < 7
    ):
        number_of_gold_coins += bet_amount
        print("骰子1点数为%d,骰子2点数为%d" % (dice_point_number_1, dice_point_number_2))
        print("恭喜你!你赢得了%d个金币!,你现在有%d个金币" % (bet_amount, number_of_gold_coins))
    else:
        number_of_gold_coins -= bet_amount
        print("骰子1点数为%d,骰子2点数为%d" % (dice_point_number_1, dice_point_number_2))
        print("很不幸!你失去了%d个金币!,你现在有%d个金币" % (bet_amount, number_of_gold_coins))
    confirmation_in_the_next_game = input("是否继续游戏?\ny/n\n")
    if confirmation_in_the_next_game == "n" or confirmation_in_the_next_game == "N":
        break
print("您的剩余金币为%d,欢迎下次再来!" % number_of_gold_coins)
