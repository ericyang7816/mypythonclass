f = open('1.txt', 'r')
for eachline in f:
    if eachline.startswith('#'):
        continue #跳过注释行
    elif '#' in eachline:
        loc = eachline.find('#')
        print(eachline[:loc])
    else:
        print(eachline, end='')  # 消除空行
f.close()
