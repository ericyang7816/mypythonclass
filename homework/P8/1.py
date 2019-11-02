f=open('1.txt','r')  
for eachline in f:  
    if eachline.startswith('#'):  
        continue  
    elif '#' in eachline:  
        loc=eachline.find('#')  
        print (eachline[:loc])  
    else:  
        print(eachline,end='') #消除空行
f.close()  
