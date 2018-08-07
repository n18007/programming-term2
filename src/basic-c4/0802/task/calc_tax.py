# 消費税率
TAX_RATE = 8

def calc_incl_tax(excl_tax):
    # 計算した税込金額を返す
    return round(excl_tax * (1 + TAX_RATE / 100))

if __name__ == '__main__':
    print(calc_incl_tax(100))
