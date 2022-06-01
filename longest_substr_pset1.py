# -*- coding: utf-8 -*-
"""
Charles Truscott, I love MIT
runfile('C:/Users/Charles_Truscott/.spyder-py3/temp.py', wdir='C:/Users/Charles_Truscott/.spyder-py3')
[0, 3, 5, 7, 8, 10, 12, 13]
Found another match: z
Found another match: c
Found another match: b
Found another match: o
Found another match: b
Found another match: o
Found another match: b
Found another match: e
Found another match: g
Found another match: g
Found another match: h
Found another match: k
Found another match: l
Traceback (most recent call last):

  File ~\.spyder-py3\temp.py:28 in <module>
    if s[n] < s[n + min_num]:

IndexError: string index out of range


"""
import re

s = 'azcbobobegghakl'
found_alphabetic_match = False
is_greatest_length = False
consecutive_alphabetic_list = []
num_posn = []
num_posn_end = []
counter = 0
counter_plus_one = 1
consecutive_found = False
for n in range(0, len(s) - 1):
    if s[counter] < s[counter + 1]:
        consecutive_found = True    
        num_posn += [counter]
    counter += 1
print(num_posn)
max_num = 26
min_num = 0
for n in num_posn:
    while min_num <= max_num:
        if s[n] < s[n + min_num]:
            print("Found another match: {}".format(s[n + min_num]))
        min_num += 1

    
        

    
