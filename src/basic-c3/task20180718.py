# coding: UTF-8
import sys

# 登場するメニューを定義
main_menus = {
    "DripCoffee": 280,
    "ColdBrewCoffee": 320,
    "CafeLatte": 330,
    "SoyLatte": 380,
    "Cappuccino": 330,
    "CaramelFrappuccino": 470,
    "MacchaCreamFrappuccino": 470
}

option_menus = {
    "LowFatMilk": 0,
    "NonFatMilk": 0,
    "SoyMilk": 50,
    "DeepCoffee": 60,
    "WhipCream": 70,
    "CaramelShrup": 60,
    "ChocoSource": 0,
    "DeCafe": 50
}

ordered = []
sum_v = 0

print("スターばっぺーへようこそ")

# メインメニューを注文
is_main_ordering = True
while is_main_ordering:
    # メインメニューの入力
    input_v = input("メインメニューを選択してください。>>> ")

    # キャンセルされたかどうか
    if input_v == "" or input_v == "q":
        print("注文がキャンセルされました")
        sys.exit()

    if input_v in main_menus:
        sum_v += main_menus[input_v]
        ordered.append(input_v)
        is_main_ordering = False
        print("メインメニューの注文を承りました。")
    else:
        print("申し訳ありません。そのようなメニューはありません。")

# オプションメニューを注文
additional_msg = ""
while True:
    # 「他に」の文言の表示判断
    if len(ordered) > 1:
        additional_msg = "他に"

    # オプションメニューの入力
    input_v = input(additional_msg + "オプションメニューのご注文はございますか？>>> ")

    # 注文を終えるかどうか
    if input_v == "" or input_v == "q":
        break

    if input_v in option_menus:
        sum_v += option_menus[input_v]
        ordered.append(input_v)
    else:
        print("申し訳ありません。そのようなオプションはありません。")

print("ご注文内容は", ordered, "です。")
print("合計金額は{0}円です。右奥のカウンターにてお待ちください。".format(sum_v))
