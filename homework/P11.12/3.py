def min2(x, y): return x if x < y else y
def max2(y, x): return y if x < y else x


print(min2(4, 8))
print(max2(8, 4))


def my_max(*l):
    retval = l[0]
    for i in l:
        retval = max2(retval, i)
    return retval


def my_min(*l):
    retval = l[0]
    for i in l:
        retval = min2(retval, i)
    return retval


print(my_max(1, 9, 4))
print(my_max('av', 'bd', 'fd'))
print(my_min(1, 9, 4))
print(my_min('av', 'bd', 'fd'))
