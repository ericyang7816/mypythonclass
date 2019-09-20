
a=int(input("Please enter"))
b=int(input("Please enter"))
c=int(input("Please enter"))
d=0
if a>b:
    d=a
    a=b
    b=d
if b>c:
    d=b
    b=c
    c=d
if a>b:
    d=a
    a=b
    b=d
if b>c:
    d=b
    b=c
    c=d
print(a)
print(b)
print(c)

a=int(input("Please enter"))
b=int(input("Please enter"))
c=int(input("Please enter"))
d=0
if a<b:
    d=a
    a=b
    b=d
if b<c:
    d=b
    b=c
    c=d
if a<b:
    d=a
    a=b
    b=d
if b<c:
    d=b
    b=c
    c=d
print(a)
print(b)
print(c)

e=int(input("Please enter"))
f=int(input("Please enter"))
g=int(input("Please enter"))
h=int(input("Please enter"))
i=int(input("Please enter"))
choice=input("Please enter")
sum=e+f+g+h+i
if choice=='1':
    print(sum)
if choice=='2':
    avg=float(sum/5)
    print(avg)
if choice=='x':
    exit(0)

myfile=open("FILE.txt",'r')
print(myfile.read())
myfile.close()
