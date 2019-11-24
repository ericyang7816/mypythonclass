import time
class CreditCard():
    def __init__(self, balance, credit):
        self.balance = 0
        self.credit = 15000
        self.record = []

    @staticmethod
    def user_select():
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

    def transaction(self,type,money):
        item={}
        item['time']=time.time()
        item['type']=type
        item['amount']=money
        self.record.append(item)

    @staticmethod
    def valid_money_draw():
        while True:
            money = int(input('请输入金额： (100的整数倍)'))
            if money % 100 != 0 or money < 0:
                print('金额有误，请重新输入')
            else:
                return money

    def draw_credit(self):
        flag = 0
        while True:
            money = CreditCard.valid_money_draw()
            if money < self.credit:
                print('您的额度不足，是否重新输入(Y/N)：')
                choice1 = CreditCard.user_select()
                if choice1 == 1:
                    pass
                else:
                    flag = 1
        if flag == 0:
            print('取现金额：%d 元,手续费：%d 元' % money, 0.05*money)
            print('是否确认取现? (Y/N)')
            choice2 = CreditCard.user_select()
            if choice2 == 1:
                if 0.05*money > self.balance:
                    print('手续费扣除失败，余额不足')
                else:
                    self.credit -= money
                    self.balance -= money*0.05
                    pass
            else:
                pass

    def draw_balance(self):
        flag = 0
        while True:
            money = CreditCard.valid_money_draw()
            if money < self.balance:
                print('您的余额不足，是否重新输入(Y/N)：')
                choice1 = CreditCard.user_select()
                if choice1 == 1:
                    pass
                else:
                    flag = 1
        if flag == 0:
            self.balance -= money
            pass

    def pay(self):
        while True:
            money = int(input('请输入金额：'))
            if money < 0:
                print('金额有误，请重新输入')
            else:
                break
        if money < self.credit:
            print('信用额度不足')
        else:
            self.credit-=money
            self.transaction('pay',money)
