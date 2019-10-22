#!/usr/bin/python
nums = input("Please enter some numbers,separate by space:")
splitNums=nums.split(" ") #按空格分隔

numList = []
for n in splitNums:
    numList.append(int(n)) #转换为数字
sortedList = sorted(numList)

dictList = []
for n in splitNums:
    dictList.append(n)
sortedDictList = sorted(dictList)

print(sortedList)
print(sortedDictList)

'''
nums=input("Please enter your numbers:")
list1nums=list(nums)
list.sort(list1nums,reverse=True)

print(list1nums)
list2nums=list(str(nums))
list.sort(list2nums,reverse=True)

print(list2nums)
'''

