from operator import add,sub
from random import randint,choice
ops={'+':add,'-':sub}
def init():
    op=choice('+-')
    nums=[randint(1,10) for x in range(2)]
    nums.sort(reverse=True)

    ans=ops[op](*nums)
    pr='%d %s %d=' % (nums[0],op,nums[1])
    oops=0
    while True:
        try:
            if int(input(pr))==ans:
                print('correct')
                break
            if oops==2:
                print('answrer:\n%s %d'% (pr,ans))
            else :
                print('incorrect... try again')
                oops+=1
        except(KeyboardInterrupt,EOFError,ValueError):
            print('invalid input... try again')
def main():
    while True:
        init()
        try:
            opt=input('Again [y/n]?').lower()
            if opt and opt[0]=='n':
                break
        except(KeyboardInterrupt,EOFError):
            break
if __name__=='__main__':
    main()