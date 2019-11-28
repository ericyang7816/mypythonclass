def menu(mycard):  # 修改了第八章作业的代码
    prompt = """
                Welcome:
    (S)how account   (B)alance withdraw
    (P)ay            (C)redit withdraw
    (D)eposit        (R)epayment
                (Q)uit 
    
            Have a nice day!
    Please select: """

    done = False

    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)
            print('\n')
            if choice not in 'spdbcrq':
                print('invalid option, try again')
            else:
                chosen = True
        if choice == 's':
            mycard.show()
        if choice == 'p':
            mycard.pay()
        if choice == 'd':
            mycard.deposit()
        if choice == 'b':
            mycard.draw_balance()
        if choice == 'c':
            mycard.draw_credit()
        if choice == 'r':
            mycard.repayment()
        if choice == 'q':
            done = True
