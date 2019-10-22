#!/usr/bin/python

import string
import keyword
alphas = string.ascii_letters+'_'
nums = string.digits
str=input("Please enter a id:")

if str in keyword.kwlist:
    print("Invalid ID.The ID is a key word.")
else:
    if len(str)==1:
        if str[0] not in alphas:
            print("Invalid ID.First symbol must be alphabetic.")
        else:
            print("Valid ID.")
    else:
        flag=0
        if str[0] not in alphas:
            print("Invalid ID.First symbol must be alphabetic.")
            flag=1
        else:
            for otherChar in str[1:]:
                if otherChar not in alphas+nums:
                    print("Invalid ID.Other symbol(s) must be alphabetic.")
                    flag=1
                    break
        if flag==0:
            print("Valid ID")