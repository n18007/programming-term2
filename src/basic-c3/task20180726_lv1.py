# coding: UTF-8
import random

cur_x = 0   # 現在の横位置

def shake_dice():
    """
    サイコロを振る

    Parameters
    ----------
    なし

    Returns
    -------
    出た目の数
    """
    return random.randint(1, 6)

def go_forward(moving_cells):
    """
    前に進む

    Parameters
    ----------
    moving_cells : int
        進むマス目

    Returns
    -------
    なし
    """
    global cur_x
    cur_x += moving_cells
    msg = "{0}が出ました。".format(moving_cells)
    if cur_x >= 10:
        msg += "おめでとうございます。ゴールしました!"
    else:
        msg += "現在位置は{0}です。".format(cur_x)

    print(msg)

while cur_x < 10:
    _ = input("サイコロを振ってください")
    go_forward(shake_dice())
