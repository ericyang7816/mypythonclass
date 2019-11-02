F1 = input('pls input a file name:')
F2 = input('pls input a file name:')
f1 = open(F1, 'r')
f1alllines = f1.readlines()
f1.close()
f2 = open(F2, 'r')
f2alllines = f2.readlines()
f2.close()
len1 = len(f1alllines)
len2 = len(f2alllines)

smallfile = len1 if len1 <= len2 else len2
flag = 0
for i in range(smallfile):
    if f1alllines[i] != f2alllines[i]:
        len3 = len(f1alllines[i])
        len4 = len(f2alllines[i])
        smallstr = len3 if len3 <= len4 else len4
        for j in range(smallstr):
            if f1alllines[i][j] != f2alllines[i][j]:
                print('Difference in row %d, column %d' % (i+1, j+1))
                flag = 1
                break
            else:
                continue
if flag == 0:
    print('Equal.')
