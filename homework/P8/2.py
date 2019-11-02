N=int(input('Please enter the number of line(s): '))
F=input('Please enter the file name: ')
f=open(F,'r')
lines=f.readlines()
for i in range(N):
    print(lines[i],end='')
f.close()
