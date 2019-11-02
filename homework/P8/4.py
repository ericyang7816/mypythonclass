value = int(input('input a value between 0 and 255:'))
filename = input('input a filename:')

ch = chr(value)
f = open(filename)
print(sum(iterm.count(ch) for iterm in f))
f.close()
