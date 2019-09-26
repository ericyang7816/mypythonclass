number1=1
number2=1
index=1
print(number1)
print(number2)
while index<19:
    number3=number1+number2
    print(number3)
    index+=1
    number1=number2
    number2=number3

for i in range(2,101):
    flag=0
    for j in range(2,i):
        if i%j==1:
            flag=1
            break
    if flag==0:
        print(i)