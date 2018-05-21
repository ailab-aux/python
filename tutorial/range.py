#!/usr/bin/env python3

# range()内置函数产生数值序列。

# range()会生成一个等差级数链表。
#和切片一样，有三个参数 range(start, end, step)
# range(x) = range(0, x, 1)
# range(b, e) = range(b, e, 1)
# range(b, e, s) = range(b, e, s)
print(range(10))
print(list(range(10)))
for i in range(10):
  print(i, end=",")


