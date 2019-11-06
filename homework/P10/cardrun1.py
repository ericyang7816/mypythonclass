#!/usr/bin/env python


def safe_float(object):
    'safe version of float()'
    try:
        retval = float(object)
    except (TypeError, ValueError) as diag:
        retval = str(diag)
    finally:
        return retval


def main():
    'handles all the data processing'
    log = open('cardlog.txt', 'w')
    try:
        ccfile = open('carddata.txt', 'r')
    except IOError:
        log.write('No transactions this month \n')
        log.close()
        return
    finally:
        transactions = ccfile.readlines()
        ccfile.close()
    total = 0.00
    log.write('account log:\n')

    for each_txns in transactions:
        result = safe_float(each_txns)
        if isinstance(result, float):
            total += result
            log.write('data...processed\n')
        else:
            log.write('ignored: %s' % result)
    print('$%.2f (new balance)'%total)
    log.close()

if __name__ == '__main__':
    main()
