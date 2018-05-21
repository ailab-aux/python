#!/usr/bin/env python3

# 函数

#没有显式返回的函数，返回None，内置的一个变量。
def fib(n):
  #以下是函数的说明，可以用docstring进行build并查看。
  '''打印斐波那契数列'''
  a, b = 0, 1
  while b < n:
    print(b, end=' ')
    a, b = b, a + b

fib(2000)
print('')

#有返回值的返回返回值。
def fib2(n):
  out = []
  a, b = 0, 1
  while b < n:
    out.append(b)
    a, b = b, a + b
  return out

print(fib2(2000))

#函数变量
fib
f = fib
f(1000)
print('')

#函数内部作用域不可修改全局的变量，如需修改需要指定global关键字？
#todo 需要后续对 global local nonlocal关键字进行深入学习。
gx = 1000
def modify():
  global gx
  gx = 10
  print(gx)

modify()