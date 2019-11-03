import os  
pymodules={}  
path=r"C:\Users\Yang\.vscode\extensions\ms-python.python-2019.10.44104\pythonFiles"
pyfiles=[f for f in os.listdir(path) if f.endswith('.py')]  
for f in pyfiles:  
    module=f[:-3]  
    pymodules.setdefault(module,'')  
    pyfile=path+os.sep+f  
    fobj=open(pyfile,encoding='utf-8')  
    doc=False  
    for line in fobj:  
        if line.strip().startswith('"""''"""') and line.strip().endswith('"""'):  
            pymodules[module]+=line  
            fobj.close()  
            break  
        elif (line.strip().startswith('"""''"""') or line.strip().startswith('r"""')) and len(line)>3: 
            doc=True 
            pymodules[module]+=line 
            continue 
        elif doc: 
            if line=='"""':  
                pymodules[module]+=line  
                fobj.close()  
                doc=False  
                break  
            else:  
                pymodules[module]+=line  
        else:  
            continue  
    else:  
        fobj.close()  
           
hasdoc=[]  
nodoc=[]  
for module in pymodules:  
    if pymodules[module]:  
        hasdoc.append(module)  
    else:  
        nodoc.append(module)  
  
print ('module has no doc:')  
for key in nodoc:  
    print (key),  
print ('\n')  
print ('module has doc:')  
for key in hasdoc:  
    print ('module:',key) 
    print ('doc:',pymodules[key])  
