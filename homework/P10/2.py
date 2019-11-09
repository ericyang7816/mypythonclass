import os
alllines = []  # 临时存储编辑内容的数组


def newfile():
    while True:  # 利用系统函数处理异常
        filename = input("Please enter a name: ")
        if os.path.exists(filename):
            print("Error %s is already exist" % filename)
        else:
            break
    f = open(filename, 'w')
    content = []  # 存储键入内容的数组
    print('Please input by line,quit by press q')
    while True:
        line = input('>>')
        if line != 'q':
            content.append(line)
        else:  # 确认用户是否退出，或只是输入字母
            choice = input('---Quit: Y---\n---Input as q: N---').upper()
            if choice == 'Y':
                break
            elif choice == 'N':
                content.append(line)
            else:
                continue
    for line in content:  # 写入文件并换行
        f.write(line+'\n')
    f.close()


def displayfile():
    filename = input('Please input a file name: ')
    try:
        f = open(filename, 'r')
    except IOError as e:  # 利用try-else处理异常
        print(e)
    else:
        for line in f:
            print(line, end='')  # 去掉print()自带的换行符
        f.close()


def editfile():
    while True:  # 利用系统函数处理异常
        filename = input("Please enter a name: ")
        if not os.path.exists(filename):
            print("Error %s not found." % filename)
        else:
            f = open(filename, 'r')
            global alllines  # 声明全局变量，以便重复使用
            alllines = f.readlines()
            break
    while True:
        index = int(input('Please input the line: '))
        text = input('Please input the content: ')
        num = alllines[len(alllines)-1].count('\n')
        if index > (len(alllines)): #当最后一行末尾有换行符时，就少换一行
            extraLine = index-len(alllines)-num
            for _ in range(extraLine):
                alllines.append('\n')
            alllines.append(text+'\n')
        else:
            try: #修改第n行文件
                alllines[int(index)-1] = text+'\n'
            except: #输入行数不合法时报错
                print('Out of range.Please retry')
            else:
                pass
        choice = input('Countinue? Y/N ').upper() 
        if choice == 'N':
            break
    f.close()


def savefile(): #将alllines中的内容保存回文件
    filename = input('Please input the file name: ')
    f = open(filename, 'w')
    for line in alllines:
        f.write(line)
    f.close()


def main(): #修改了第七章作业的代码
    prompt = """
    Welcome:
    (N)ew File
    (D)isplay a File
    (E)dit a File
    (S)ave a File
    (Q)uit 
    
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
            if choice not in 'ndesq':
                print('invalid option, try again')
            else:
                chosen = True
        if choice == 'n':
            newfile()
        if choice == 'd':
            displayfile()
        if choice == 'e':
            editfile()
        if choice == 's':
            savefile()
        if choice == 'q':
            done = True
    
if __name__ == '__main__':
    main()
