"""_summary_"""

import random
import sys

gold_coins = 10
WRONG_TEXT = "请输入正确的字符！"
pay_confirm = input("您的初始金币为10个,是否充值?\ny/n\n")
while pay_confirm not in ["y", "Y", "n", "N"]:
    print(WRONG_TEXT)
    pay_confirm = input()
if pay_confirm in ["y", "Y"]:
    pay_amount = input("请输入充值金额:")
    while pay_amount.isdigit() is False:
        print("请输入正确的数量!")
        pay_amount = input()
    gold_coins += int(pay_amount)
    print(f"您已充值{pay_amount}个金币!您的金币总数为{gold_coins}!")
while True:
    bet_confirm = input("请下注!\n1-大\n2-小\n")
    while bet_confirm not in ["1", "2"]:
        print(WRONG_TEXT)
        bet_confirm = input()
    bet_amount = input("请输入下注金额:")
    while bet_amount.isdigit() is False or int(bet_amount) > gold_coins:
        print(WRONG_TEXT)
        bet_amount = input()
    bet_amount = int(bet_amount)
    dice_point = [random.randint(1, 6) for i in range(2)]
    if (bet_confirm == "1" and sum(dice_point) > 6) or (
        bet_confirm == "2" and sum(dice_point) < 7
    ):
        gold_coins += bet_amount
        print(
            f"骰子1点数为{dice_point[0]},骰子2点数为{dice_point[1]},总点数为{sum(dice_point)}"
        )
        print(f"恭喜你!你赢得了{bet_amount}个金币!,你现在有{gold_coins}个金币")
    else:
        gold_coins -= bet_amount
        print(
            f"骰子1点数为{dice_point[0]},骰子2点数为{dice_point[1]},总点数为{sum(dice_point)}"
        )
        print(f"很不幸!你失去了{bet_amount}个金币!,你现在有{gold_coins}个金币")
    if gold_coins == 0:
        pay_amount = input("您的金币已不足,请输入充值金额或输入q退出\n")
        while (pay_amount not in ["q", "Q"]) and (pay_amount.isdigit() is False):
            print(WRONG_TEXT)
            pay_amount = input()
        if pay_amount in ["q", "Q"]:
            sys.exit(0)
        else:
            gold_coins += int(pay_amount)
            print(f"您已充值{pay_amount}个金币!您的金币总数为{gold_coins}!")
    next_game_confirm = input("是否继续游戏?\ny/n\n")
    while next_game_confirm not in ["y", "Y", "n", "N"]:
        print(WRONG_TEXT)
        next_game_confirm = input()
    if next_game_confirm in ["n", "N"]:
        print(f"您的剩余金币为{gold_coins},欢迎下次再来!")
        sys.exit(0)


