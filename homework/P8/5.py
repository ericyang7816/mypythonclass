F1 = input('Please input a file name:')
F2 = input('Please input a file name:')
f1 = open(F1, 'r')
f1alllines = f1.readlines()
f1.close()
f2 = open(F2, 'r')
f2alllines = f2.readlines()
f2.close()
len1 = len(f1alllines)
len2 = len(f2alllines)  # 读取文件的操作

smallfile = len1 if len1 <= len2 else len2
flag = 0  # 修改了逻辑，增加flag在循环后判断是否相等
for i in range(smallfile):
    if f1alllines[i] != f2alllines[i]:
        len3 = len(f1alllines[i])
        len4 = len(f2alllines[i])
        smallstr = len3 if len3 <= len4 else len4
        for j in range(smallstr):
            if f1alllines[i][j] != f2alllines[i][j]:
                print('Difference in row %d, column %d' % (i+1, j+1))
                # 同时输出行列数，并让行列数以1开头
                flag = 1
                break
            else:
                continue
        if len3 < len4: #列数不相等的情况下
            if f2alllines[i][j+1]!='\n': #检查是否为换行符导致的
                print('Difference in row %d, column %d' % (i+1, j+2)) #下一列不同
                flag = 1
        else:
            if f1alllines[i][j+1]!='\n':
                print('Difference in row %d, column %d' % (i+1, j+2))
                flag = 1
            
if len1 != len2: #列数不相等的情况下
    print('Difference in row %d, column 1' % (i+2)) #下一行第一列不同
    flag = 1
if flag == 0:
    print('Equal files.')
