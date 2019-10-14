'''
第五章作业 5-4
2019.10.11
'''
year=int(input("Please enter a year:"))
if year%4==0 and year%100!=0:
    print("%d is a leap year." % year)
elif year%400==0:
    print("%d is a leap year." % year)
else:
    print("%d is not a leap year." % year)