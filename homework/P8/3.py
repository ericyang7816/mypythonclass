F=input('Please input a file name: ')  
f=open(F,'r')  
lines=f.readlines() 
print('Number of line(s): '+str(len(lines))) #使用+连接时要将后者转为字符
f.close() 
