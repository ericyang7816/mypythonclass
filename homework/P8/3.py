F=input('Please input a file name: ')  
f=open(F,'r')  
lines=f.readlines() 
print('Number of line(s): '+str(len(lines)))
f.close() 
