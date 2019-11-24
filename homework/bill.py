def bill(card):
    try:
        fobj=open('bill.log','a+')
    except IOError as e:
        print(e)
    else:
        fobj.writelines(card.record)
    finally:
        pass