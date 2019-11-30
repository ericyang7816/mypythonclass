from card import *
from menu import *
import datetime

mycard=CreditCard(1000.00,15000.00)

while True:
    date=datetime.datetime.now()
    if date.day==30:
        mycard.bill()
        print('Notice: 还款日到了！账单已出，请及时还款！')
        menu(mycard)
    else:
        menu(mycard)
