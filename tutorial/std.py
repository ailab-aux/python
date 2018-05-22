#!/usr/bin/env python3

# 标准库

#1. 操作系统接口
import os

cwd = os.getcwd()
print(cwd)

os.chdir('/home/aux/study/')
os.chdir(cwd)

os.system('mkdir hello')

#WARNING: 应该用 import os 风格而非 from os import *。这样可以保证随操作系统不同而有所变化的 os.open() 不会覆盖内置函数 open()。
#
# 在使用一些像 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:
l = dir(os)
for i, v in enumerate(l):
  print(v)

print(help(os))