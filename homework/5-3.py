'''
第五章作业 5-3
2019.10.11
'''
def Score(num):
    if 90<=num<=100:
        print('A')
    elif 80<=num<=89:
        print('B')
    elif 70<=num<=79:
        print('C')
    elif 60<=num<=69:
        print('D')
    elif num>=0 and num<60:
        print('F')
    else:
        print("Wrong number")
        
print("Please enter the score.")
num=int(input(">>"))
Score(num)
