from random import randint


def leapyear(year):
    if year < 1900 or year > 2016:
        print('year error')
    elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return year


years = []
for i in range(10):
    years.append(randint(1900, 2016))
print(years)
print(list(filter(leapyear, years)))
# 列表解析
print([n for n in [randint(1900, 2016) for i in range(10)] if (
    (n % 4 == 0 and n % 100 != 0) or (n % 4 == 0 and n % 100 == 0))])
