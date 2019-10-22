#!/usr/bin/python
import string
i=0
j=0
k=0
courses=['高等数学','概率论与数理统计','统计学','Python程序设计','计算机网络', '数据库系统','数据结构与算法','管理学原理','计算机基础','逻辑学']
for i in range(len(courses)):
    if '数' in courses[i]:
        print(courses[i])
print('-------------')
for i in range(len(courses)):
    if 'Python程序设计'== courses[i]:
        print(courses[i])
print('-------------')
for i in range(len(courses)):
    if 'Python程序设计'!= courses[i]:
        print(courses[i])
print('-------------')
numDayCourses = 6
monday = ['高等数学  ', '高等数学  ', '电子商务  ', '电子商务  ', 'Python编程', 'Python编程']
tuesday = ['计算机基础', '计算机基础','离散数学  ', '离散数学  ', '电子商务  ', '电子商务  ']
wednesday = ['管理学原理', '管理学原理','计算机基础', '计算机基础','高等数学  ', '高等数学  ']
thursday = ['思想政治  ', '思想政治  ','大学英语  ', '大学英语  ','专业实践  ', '专业实践  ']
friday = ['Python编程', 'Python编程', '离散数学', '离散数学','大学英语', '大学英语']
week = [monday,tuesday,wednesday,thursday,friday]
print('节 ','星期一      ','星期二      ','星期三      ','星期四      ','星期五    ')
print("")
for i in range(0,6):
    print (i+1,end='   ')
    for j in range(len(week)):
       print (week[j][i],end='   ')
    print("\n")
    
