# -*- coding: utf-8 -*-

from flask import Flask, render_template
from grs import Stock, BestFourPoint

app = Flask(__name__)

stock_list = [
    '2330',  # 台積電
    '2317',  # 鴻海
    '1301',  # 台塑
    '1326',  # 台化
    '2412',  # 中華電
    '3008',  # 大立光
    '1303',  # 南亞
    '2308',  # 台達電
    '2454',  # 聯發科
    '2881',  # 富邦金
]

stock_name = {
    '2330': u'台積電',
    '2317': u'鴻海',
    '1301': u'台塑',
    '1326': u'台化',
    '2412': u'中華電',
    '3008': u'大立光',
    '1303': u'南亞',
    '2308': u'台達電',
    '2454': u'聯發科',
    '2881': u'富邦金',
}


@app.route('/')
def stocker():
    st = {}
    for stock in stock_list:
        s = Stock(stock)
        b = BestFourPoint(s)
        bfp = b.best_four_point()
        buy_or_sell = "hmmmm, don't touch"
        if bfp and bfp[0] is True:
            buy_or_sell = "Buy it."
        elif bfp and bfp[0] is False:
            buy_or_sell = "Sell it."

        st[stock] = {'pivot': buy_or_sell, 'price': s.price[-5:]}

    return render_template('stocker.html', stock=st, name=stock_name)


if __name__ == '__main__':
    app.run()
