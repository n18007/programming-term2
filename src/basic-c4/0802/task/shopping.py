import calc_tax

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
    total_ex_tax = 0    # 税抜き合計
    res_list = []   # 結果として返すリスト

    for name, price in unit_dc.items():
        # TODO:各商品の小計をメッセージとして格納(passは仮のコードなので削除すること)
        pass

    # TODO:税抜き総額と、消費税計算した税込み総額を得る
    # TODO:残金を算出する

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
