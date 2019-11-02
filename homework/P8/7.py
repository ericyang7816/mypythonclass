import os  
file1=input('input first file name:')  
file2=input('input second file name:')  
  
f1=open(file1,'r')  
f2=open(file2,'a+')  
f2.write(os.linesep)  
for line in f1:  
    f2.write(line)  
f1.close()  
f2.close()  
