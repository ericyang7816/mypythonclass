import time
import json


class CreditCard():
    def __init__(self, balance, credit):
        self.balance = balance  # 账户余额
        self.credit = credit  # 信用额度
        self.record = []  # 交易记录
        self.total_deal = 0  # 交易数量

    @staticmethod
    def user_select():  # 用户选择
        chosen = False
        while not chosen:
            try:
                choice = input('>>').strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                print('Error, try again')
            if choice not in 'yn':
                print('invalid option, try again')
            else:
                chosen = True
        if choice == 'y':
            return 1
        elif choice == 'n':
            return 0

    def transaction(self, type, money):
        item = {}
        item['code'] = self.total_deal+1
        item['time'] = time.asctime(time.localtime(time.time()))
        item['type'] = type
        item['amount'] = money
        item['interest'] = 0
        self.record.append(item)
        self.total_deal += 1

    @staticmethod
    def valid_money_atm():
        while True:  # 实现自动取款机的操作
            money = int(input('请输入金额 (100的整数倍)： '))
            if money % 100 != 0 or money < 0:
                print('金额有误，请重新输入')
            else:
                return money

    @staticmethod
    def safe_float_num(num):
        try:
            return float(num)
        except(TypeError, ValueError) as e:
            print(e)  # 当转换出错时输出错误
            return None

    def show(self):  # 显示账户的余额和额度
        print('当前账户余额为：%d' % self.balance)
        print('当前可用信用额度为：%d' % self.credit)

    def draw_credit(self):
        flag = 0
        while True:
            money = CreditCard.valid_money_atm()
            if money > self.credit:
                print('您的额度不足，是否重新输入 (Y/N)：')
                choice1 = CreditCard.user_select()
                if choice1 == 1:
                    pass
                else:
                    flag = 1
                    break
            else:
                break
        if flag == 0:
            print('取现金额：%d 元,手续费：%d 元' % (money, 0.05*money))
            print('是否确认取现? (Y/N)')
            choice2 = CreditCard.user_select()
            if choice2 == 1:
                if 0.05*money > self.balance:
                    print('手续费扣除失败，余额不足')
                else:
                    self.credit -= money
                    self.balance -= money*0.05
                    self.transaction('draw_credit', money)
                    self.transaction('fee', money*0.05)
                    print('取现成功！')
            else:
                pass

    def draw_balance(self):
        flag = 0
        while True:
            money = CreditCard.valid_money_atm()
            if money > self.balance:
                print('您的余额不足，是否重新输入(Y/N)：')
                choice1 = CreditCard.user_select()
                if choice1 == 1:
                    pass
                else:
                    flag = 1
                    break
            else:
                break
        if flag == 0:
            self.balance -= money
            self.transaction('draw_balance', money)
            print('提现成功！')

    def pay(self):
        while True:
            money = CreditCard.safe_float_num(input('请输入金额：'))
            if money < 0:
                print('金额有误，请重新输入')
            else:
                break
        if money > self.credit:
            print('信用额度不足')
        else:
            self.credit -= money
            self.transaction('pay', money)
            print('支付成功！')

    def deposit(self):
        money = self.valid_money_atm()
        self.balance += money
        self.transaction('deposit', money)
        print('存款成功！')

    def repayment(self):
        money_need_pay = 15000-self.credit
        print('您的待还余额为：%d' % money_need_pay)
        while True:
            money = CreditCard.safe_float_num(input('请输入还款金额：'))
            if money < 0:
                print('金额有误，请重新输入')
            elif money > money_need_pay:
                print('您太有钱了，不用还这么多')
            else:
                self.credit += money
                self.transaction('repay', money)
                print('还款成功！')
                break

    def bill(self):
        try:
            fobj = open('bill.log', 'a+')
        except IOError as e:
            print(e)
        else:
            for rec in self.record:
                str_rec = json.dumps(rec, ensure_ascii=False)
                fobj.write(str_rec+'\n')
