def calcAvgPE(funds):
    for item in funds:
        amount_ratio = {}  # 字典存储基金的持仓金额占比
        sum_price = 0
        avg_pe = 0
        sum = 0
        for stock in item['shares']:
            sum_price += stock['price']*stock['number']
        for stock in item['shares']:  # 求出持仓金额占比
            amount_ratio[stock['code']] = stock['price'] * \
                stock['number']/sum_price
        for stock in item['shares']:
            sum += amount_ratio[stock['code']]/stock['pe']
        avg_pe = 1/sum
        print(item['name']+' '+str(avg_pe))


def sortedPECode(funds):
    for item in funds: # 利用市盈率作为关键字排序
        print(sorted(item['shares'], key=lambda a: a['pe']))
