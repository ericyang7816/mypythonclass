'''
2 ways to print prime numbers from 1 to 100
Yang 2019.09.27
'''

i=2
for i in range(2,101):
    flag=0
    j=2
    for j in range(2,i):
        if i%j==0:
            flag=1
            break 
    if flag==0:
        print(i)

num=[]
i=2
for i in range(2,100):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)
