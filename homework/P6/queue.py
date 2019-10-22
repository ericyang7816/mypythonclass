#queue.py
queue=[]

def enQ():
    queue.append(input('enter new string'))

def deQ():
    if len(queue)==0:
        print("this queue is empty ,you can't pop")
    print("removed[",queue.pop(0),"]\n")

def viewQ():
    print(queue)

CMDs={'e':enQ,'d':deQ,'v':viewQ}

hint='''
(E)nqueue
(D)equeue
(v)iew
(Q)uit

Enter choice: '''
while True:
    while True:
        try :choice=input(hint).strip().lower()
        except(IOError,KeyboardInterrupt,IndexError):
            choice='q'
        print("your picked ",choice)
        if choice not in 'edvq':
            print("invalid input ,enter again")
        else:
            break
    if choice=='q':
        break
    CMDs[choice]()