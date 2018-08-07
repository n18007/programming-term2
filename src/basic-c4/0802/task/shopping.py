from calc_tax import calc_incl_tax as cit

def exec():
    """
    メインロジックを実行する

    Parameters
    ----------
    なし

    Returns
    -------
    list
        表示されるメッセージを要素に含むリスト
    """

    # 単価を管理するdictionary
    unit_dc = {
        'Banana': 100,
        'Apple': 200,
        'Orange': 150
    }
    # 個数を管理するdictionary
    nums_dc = {
        'Banana': 2,
        'Apple': 1,
        'Orange': 3
    }
    money = 2000    # 所持金
    ex_tax_list = []    # 税抜き合計
    res_list = []   # 結果として返すリスト

    for name, price in unit_dc.items():
        item_total = price * nums_dc[name]
        ex_tax_list.append(item_total)
        res_list.append("{0}を{1}個買いました。商品計は{2}です。".format(name, nums_dc[name], item_total))

    # 税抜き総額と、消費税計算した税込み総額を得る
    total_incl_tax = cit(sum(ex_tax_list))
    res_list.append("総計の税抜き額は{0}円、税込額は{1}円です。".format(sum(ex_tax_list), total_incl_tax))
    # 残金を算出する
    money -= total_incl_tax
    res_list.append("残金は{0}円です。".format(money))

    return res_list

def display(msgs):
    """
    結果を表示する

    Parameters
    ----------
    msgs: list
        表示するメッセージが格納されたリスト

    Returns
    -------
    なし
    """
    print("\n".join(msgs))

# メイン処理
if __name__ == '__main__':
    display(exec())
