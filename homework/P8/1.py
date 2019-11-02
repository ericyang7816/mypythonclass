f=open('test.txt','r')  
for eachline in f:  
    if eachline.startswith('#'):  
        continue  
    elif '#' in eachline:  
        loc=eachline.find('#')  
        print (eachline[:loc])  
    else:  
        print(eachline,end='')  
f.close()  
