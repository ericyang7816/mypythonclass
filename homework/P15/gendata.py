from random import randint, choice
from string import ascii_lowercase
from sys import maxsize
from time import ctime
doms = ( 'com', 'edu', 'net', 'org', 'gov' )
f=open('redata.txt','w')
for i in range(randint(5, 10)):
    dtint = randint(0, maxsize-1) # pick date
    dtstr = ctime(dtint/10000000000) # date string
    shorter = randint(4, 7) # login shorter
    em = ''
    
    for j in range(shorter): # generate login
        em += choice(ascii_lowercase)

    longer = randint(shorter, 12) # domain longer
    dn = ''
    for j in range(longer): # create domain
        dn += choice(ascii_lowercase)
    small_dtint=dtint/10000000000
    infostr=dtstr+'::'+em+'@'+dn+'.'+choice(doms)+'::'+str(small_dtint)+'-'+str(shorter)+'-'+str(longer)+'\n'
    f.write(infostr)
    print ('%s::%s@%s.%s::%d-%d-%d' % (dtstr, em,dn, choice(doms), dtint/10000000000, shorter, longer))
