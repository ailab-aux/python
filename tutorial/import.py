#!/usr/bin/env python3

import fibo

fibo.fib(1000)

print(fibo.fib2(100))

print(fibo.__name__)

#使用变量赋值为函数
fib = fibo.fib
fib2 = fibo.fib2

fib(500)
print(fib2(1000))