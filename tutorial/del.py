#!/usr/bin/env python3

# del语句

a = [-1, 1, 66.25, 333, 333, 1234.5]
print(a)

del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

#del可以删除整个变量，删除后就无法再引用了，否则会出现错误。
# del a