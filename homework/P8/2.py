lineNum=int(input('Please enter the number of line(s): '))
fileName=input('Please enter the file name: ')
f=open(fileName,'r')
lines=f.readlines()
for i in range(lineNum):
    print(lines[i],end='') #消除空行
f.close()
