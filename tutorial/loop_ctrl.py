#!/usr/bin/env python3

# 循环控制语句

# break/continue和C语言一样。
# else用于
#   1. for循环迭代完整个列表是执行
#   2. while循环执行条件为false时执行。
#   3. 当循环被break的时候不被执行。

print(list(range(2, 2)))

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n//x)
      break;
  else:
    print(n, 'is a prime number')
