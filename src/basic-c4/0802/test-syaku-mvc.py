# モジュールのインポート
import syaku

def exec(sk):
    """
    処理を実行する

    Parameters
    ----------
    sk: int or float
        尺の値

    Returns
    -------
    float
        センチメートルの値
    """
    # モジュールの関数を使う
    return str(sk) + "尺= " + str(syaku.syaku_to_cm(sk)) + " cm"

def display(s):
    """
    文字列を表示する

    Parameters
    ----------
    s: str
        表示する文字列

    Returns
    -------
    なし
    """
    print(s)

print(__name__)
if __name__ == '__main__':
    display(exec(10))
    display(exec(20))
