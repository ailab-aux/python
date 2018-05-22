#!/usr/bin/env python3

# dir函数, 内置函数
# 用于按照模块名，搜索模块定义，返回一个字符串类型的存储列表。

import fibo, sys

print(dir(fibo))

for i, v in enumerate(dir(sys)):
  print(v)

# 无参数调用时， dir()函数返回当前定义的命名。

a = [1, 2, 3, 4, 5]
import fibo
fib = fibo.fib
print(dir())

# dir() 不会列出内置函数和变量名
# 如果你想列出这些内容，它们在标准模块 builtins 中定义:
import builtins
for i, v in enumerate(dir(builtins)):
  print(v)