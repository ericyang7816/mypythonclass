#!/usr/bin/env python

import time
db = {}

def newuser():
    prompt = """
---SIGN UP---
username: """
    while True:
        name = input(prompt)
        if name in db.keys():
            prompt = 'not available, try another: '
            continue
        else:
            break
    passwd = input('password: ')
    localTime = time.time() #获取当前格式化的时间
    info=[passwd,localTime] #创建列表
    db[name] = info #更新字典

def olduser():
    name = input('login: ')
    pwd = input('passwd: ')
    passwd = db.get(name)[0]
    if passwd == pwd:
        print('welcome back', name)
        previousTime=db.get(name)[1]
        currentTime=time.time()
        db.get(name)[1]=currentTime #读取时间，并重新存入时间
        if (currentTime-previousTime)<=14400: #判断时间是否在4小时（14400秒）内
            print("You already logged in at: ",time.asctime(time.localtime(previousTime))) #利用查到的asctime()函数生成可读的时间
    else:
        print('login incorrect')

def manageMenu():
    prompt = """
    (D)elete a User
    (S)how User
    (Q)uit
    Enter choice: """

    done = False #重用menu的部分代码
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)
            if choice not in 'dsq':
                print('invalid option, try again')
            else:
                chosen = True 
        if choice == 'q':
            done = True
        if choice == 'd':
            deleteUser()
        if choice == 's':
            showUsers()

def deleteUser():
    name=input("Please input the name: ") 
    if name not in db.keys(): #python3不支持has_key()
        print("Error.Name not found.")
    else:
        db.pop(name)
        print("Delete %s successful." % name)


def showUsers():
    for key in db:
        print("Number of users: %d" % len(db))  #返回用户数量
        print('name = %s, password = %s' %(key,db[key][0])) #返回用户信息


def showmenu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (M)anage
    (Q)uit
    Enter choice: """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print('\nYou picked: [%s]' % choice)
            if choice not in 'neqm':
                print('invalid option, try again')
            else:
                chosen = True 
        if choice == 'q':
            done = True
        if choice == 'n':
            newuser()
        if choice == 'e':
            olduser()
        if choice == 'm':
            if input("Please input the admin password:")=='123':
                manageMenu()
            else:
                print("Wrong password. Please try again.")


if __name__ == '__main__':
    showmenu()
    