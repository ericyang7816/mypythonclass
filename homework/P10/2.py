import os
alllines = []

def newfile():
    while True:
        filename = input("Please enter a name: ")
        if os.path.exists(filename):
            print("Error %s is already exist" % filename)
        else:
            break
    f = open(filename, 'w')
    content = []
    print('Please input by line,quit by press q')
    while True:
        line = input('>>')
        if line != 'q':
            content.append(line)
        else:
            choice = input('Are you sure? Y/N ').upper()
            if choice == 'Y':
                break
            else:
                content.append(line)
    for line in content:
        f.write(line+'\n')
    f.close()


def displayfile():
    filename = input('Please input a file name: ')
    try:
        f = open(filename, 'r')
    except IOError as e:
        print(e)
    else:
        for line in f:
            print(line, end='')
        f.close()


def editfile():
    while True:
        filename = input("Please enter a name: ")
        if not os.path.exists(filename):
            print("Error %s not found." % filename)
        else:
            f=open(filename,'r')
            global alllines
            alllines=f.readlines()
            break
    while True:
        index = int(input('Please input the line: '))
        text = input('Please input the content: ')
        try:
            alllines[int(index)-1]=text+'\n'
        except:
            print('Out of range.Please retry')
        else:
            choice=input('Do you want to quit? Y/N ').upper()
            if choice=='Y':
                break
    print(alllines)
    f.close()


def savefile():
    filename = input('Please input the file name: ')
    f = open(filename, 'w')
    for line in alllines:
        f.write(line)
    f.close()


def main():
    prompt = """
    Welcome:
    (N)ew File
    (D)isplay a File
    (E)dit a File
    (S)ave a File
    (Q)uit 
    
    Please select: """

    done = False

    print(prompt)
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
    '''
    while True:
        print ('\n')
        print ('1. create a file')
        print ('2. show a file')
        print ('3. edit a file')
        print ('4. save a file')
        print ('5. quit')
 
        ch=input('input a choice:')
        if ch not in '1234':
            break
        elif ch=='1':
            filename=input('input a file name:')
            create(filename)
        elif ch=='2':
            filename=input('input a file name:')
            show(filename)
        elif ch=='3':
            if filename == '':  
                filename = input('file name: ')
            index=int(input('input a index of line:'))
            content=input('pls input a line:')
            ls=edit(filename,index,content)
        elif ch=='4':
            save(filename,ls)
    '''


if __name__ == '__main__':
    main()
