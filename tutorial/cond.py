#!/usr/bin/env python3

#深入条件控制

# in/not in
# is/is not
# a < b == c: a < b && b == c
# and/or/not not > and > or
# 短路特性
# 
x, y, z = '', 'Trondheim', 'Hammer Dance'
a = x or y or z
print(a)