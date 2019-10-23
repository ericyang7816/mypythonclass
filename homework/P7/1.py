
dicta=dict(b=2,a=1,c=3)
'''
for key in sorted(dicta):  
    print(key)
'''
keys = dicta.keys() 
print(sorted(keys)) #也可以不通过循环，在一行中显示

for key in sorted(dicta):  
    print('key=%s, value=%s' %(key,dicta[key]))

listvalue = dicta.values()
for value in sorted(listvalue):  #dict_values不支持sort()的用法
    for key in dicta.keys():  
        if value == dicta[key]:  
            print('key=%s, value=%s' %(key,dicta[key]))
