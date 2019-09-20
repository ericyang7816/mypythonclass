'''
#3
a=0
while a<=10:
    print(a)
    a=a+1

for a in range(11):
    print(a)

#4
str1=input("Please input")
for i in range(len(str1)):
    print(str1[i])

i=0
while i<len(str1):
    print(str1[i])
    i=i+1

#5
list1=[1,2,3,4,5]
sum=0
for word in list1:
    sum=sum+word
print(sum)
##
for j in range(5):
    list1[j]=int(input("Please input:"))
sum=0
for word1 in list1:
    sum=sum+word1
print(sum)
##
i=0
sum=0
while i<5:
    sum=sum+int(list1[i])
    i=i+1
print(sum)

#6
list2=(1,2,5,7,9)
sum=0
for word in list2:
    sum=sum+word
avg=float(sum/5)
print(avg)

'''
flag=True
while flag==True:
    num=int(input("Please enter a number between 1 and 100"))
    if num>=1 and num<=100:
        print("OK")
        flag=False
    else:
        print("Please retry")
