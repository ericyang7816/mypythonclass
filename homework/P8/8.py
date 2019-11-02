import gzip  
#compress  
f_in=open(r'1.txt','rb')  
f_out=gzip.open(r'1.txt.gz','wb')  
f_out.writelines(f_in)  
f_out.close()  
f_in.close()  
#decompress  
f=gzip.open(r'1.txt.gz','rb')  
f_out=open(r'1.txt','wb')  
content=f.read()  
f_out.write(content)  
f.close()  
f_out.close()  
