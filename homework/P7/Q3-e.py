#!/usr/bin/env python

import time
import re
db = {}

def userLogin():
    prompt = """
---SIGN UP/IN---
Username: """
    while True:
        inputName = input(prompt)
        if not re.match("^[a-zA-Z0-9]*$", inputName): #利用第六章的正则表达式，判断用户名是否合法
            print('Special characters and blanks are not allowed.')
            prompt = 'Try another:'
            continue
        else:
            break
    flag=0 
    for i in range(len(db)):
            if inputName.lower() in str(list(db.keys())[i]).lower(): #利用循环，将用户名全部小写，查找是否存在
                name=str(list(db.keys())[i]) #读取真正用户名
                flag=1 #增加flag判断用户名是否存在
                break
     
    if flag == 0:
        print("The username does not exist.")
        chosen = False
        while not chosen:
            choice=input("Do you want to register as a new user? Y/N: ").lower() #询问用户选择
            if choice not in 'yn':
                    print('invalid option, try again')
            else:
                chosen = True
        if choice == 'y':
            passwd = input('Please enter a password: ')
            localTime = time.time() #获取当前格式化的时间
            info=[passwd,localTime] #创建列表
            db[inputName] = info #更新字典
            print("Success")
    if flag == 1:
        while True:
            passwd = input('Password: ')
            if db.get(name)[0]==passwd:
                print('Welcome back! '+name)
                previousTime=db.get(name)[1]
                currentTime=time.time()
                db.get(name)[1]=currentTime #读取时间，并重新存入时间
                if (currentTime-previousTime)<=14400: #判断时间是否在4小时（14400秒）内
                    print("You already logged in at: ",time.asctime(time.localtime(previousTime))) 
                    #利用查到的asctime()函数生成可读的时间
                break
            else:
                print('Wrong password.Please retry.')

'''
def newuser():
    prompt = """
---SIGN UP---
username: """
    while True:
        name = input(prompt)
        if not re.match("^[a-zA-Z0-9]*$", name): #利用第六章的正则表达式，判断用户名是否合法
            print('Special characters and blanks are not allowed.')
            prompt = 'Try another:'
            continue
        else:
            break
    while True:
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
    print('---SIGN IN---')
    inputName = input('Username: ')
    passwd = input('Password: ')
    for i in range(len(db)):
        if inputName.lower() in str(list(db.keys())[i]).lower(): #利用循环，将用户名全部小写，查找是否存在
            name=str(list(db.keys())[i]) #读取真正用户名
            break
    if db.get(name)[0]==passwd:
        print('Welcome back! '+name)
        previousTime=db.get(name)[1]
        currentTime=time.time()
        db.get(name)[1]=currentTime #读取时间，并重新存入时间
        if (currentTime-previousTime)<=14400: #判断时间是否在4小时（14400秒）内
            print("You already logged in at: ",time.asctime(time.localtime(previousTime))) #利用查到的asctime()函数生成可读的时间
    else:
        print('login incorrect')
'''
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
    inputName=input("Please input the name: ") 
    flag=0 
    for i in range(len(db)):
            if inputName.lower() in str(list(db.keys())[i]).lower(): #利用循环，将用户名全部小写，查找是否存在
                name=str(list(db.keys())[i]) #读取真正用户名
                flag=1 #增加flag判断用户名是否存在
                break
    if flag==0:
        print("Error.Name not found.")
    else:
        db.pop(name)
        print("Delete %s successful." % name)


def showUsers():
    print("Number of users: %d" % len(db))  #返回用户数量
    for key in db:
        print('name = %s, password = %s' %(key,db[key][0])) #返回用户信息


def showmenu(): ##重新修改的菜单
    prompt = """
    (U)ser Login
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
            if choice not in 'umq':
                print('invalid option, try again')
            else:
                chosen = True 
        if choice == 'q':
            done = True
        if choice == 'u':
            userLogin()
        if choice == 'm':
            if input("Please input the admin password:")=='123': #暂定的管理员密码
                manageMenu()
            else:
                print("Wrong password. Please try again.")


if __name__ == '__main__':
    showmenu()
    