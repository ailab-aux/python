#!/usr/bin/env python3

#深入函数。

#1. 默认函数参数
def ask_ok(prompt, retries = 4, complaint = "yes or no, please!"):
  while True:
    ok = input(prompt)
    if ok in ('y', 'ye', 'yes'):
      return True
    if ok in ('n', 'no', 'nop', 'nope'):
      return False
    retries = retries - 1
    if retries < 0:
      raise OSError('uncooperative user')
    print(complaint)

#默认参数
ok = ask_ok('Do you really want to quit?')
print(ok)

#两个参数
ok = ask_ok('OK to overwrite the file?', 2)
print(ok)

#全部参数
ok = ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')
print(ok)

#调换参数位置
ok = ask_ok('prompt string, yes or no?', complaint='what the fuck? only yes or no!!!', retries=5)
print(ok)

#WARNING: 默认值在函数定义作用域解析，不在调用作用域解析。
#下面的函数只会输出5，而不输出6.
i = 5
def f(flag = i):
  print(flag)
  return flag

i = 6
x = f()
print(x)

#WARNING: 默认值只被赋值一次，如果参数为列表等参数，则多次调用会累积。
def append_list(a, L=[]):
  L.append(a)
  return L
print('default function argument, assignment once by function define.')

print(append_list(1))
print(append_list(2))
print(append_list(3))
#output:
# [1]
# [1, 2]
# [1, 2, 3]

# 如果不想让默认值在后续调用中累积，可以如下定义函数。
def append_list2(a, L=None):
  if L is None:
    L = []
  L.append(a)
  return L

print(append_list2(1))
print(append_list2(2))
print(append_list2(3))
#output:
# [1]
# [2]
# [3]

#2. 关键字参数，上面已经提及。
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
  print("-- This parrot wouldn't", action, end=' ')
  print("if you put", voltage, "volts through it.")
  print("-- Lovely plumage, the", type)
  print("-- It's", state, "!")

#小插曲，量变到质变的过程，就是坚持的过程。
x = 1.01 ** 365
print(x)

print("------ call parrot(1000) ------")
parrot(1000)
print("------ call parrot(voltage=1000) ------")
parrot(voltage=1000)
print("------ call parrot(voltage=1000000, action='V00000M') ------")
parrot(voltage=1000000, action='V00000M')
print("------ call parrot(action='V00000M', voltage=1000000) ------")
parrot(action='V00000M', voltage=1000000)
print("------ call parrot('a million', 'bereft of life', 'jump') ------")
parrot('a million', 'bereft of life', 'jump')
print("------ call parrot('a thousand', state='pushing up the daisies') ------")
parrot('a thousand', state='pushing up the daisies')

#WARNING:关键字参数后面必须是关键字参数，下面的调用错误
# parrot(voltage=5.0, 'dead')
#WARNING:任何参数都不可以多次赋值

#关键字参数列表和字典。
# **name 字典 //无序的
# *name 列表  //有序的
# 如果函数参数两者都存在，字典必须在后面。
def cheeseshop(kind, *arguments, **keywords):
  print("-- Do you have any", kind, "?")
  print("-- I'm sorry, we're all out of", kind)
  for arg in arguments:
    print(arg)
  print("-" * 40)
  keys = sorted(keywords.keys())
  for kw in keys:
    print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#3.可变参数列表 *args 
def concat(*args, sep="/"):
  return sep.join(args)

print(concat("earth", "mars", "venus"))
print(concat("earth", "mars", "venus", sep="."))


#4.参数列表的分拆。传入参数为一个列表，但是函数需要接受分开的一个个参数值。

# 列表可以使用 `*args` 分拆一个列表为一个个独立的参数值。
list(range(3, 6))
args = [3, 6]
list(range(*args))

# 字典可以使用 `**args` 分拆变成一个个独立的关键字参数
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

#5.lambda表达式 匿名函数 
def make_incrementor(n):
  return lambda x: x + n

fl = make_incrementor(40) # x = 40.
print(fl(0))
print(fl(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# 注意key对应一个lambda表达式，key指定一个函数在每个元素比较前被调用。
# 可以理解这个匿名函数为：
# def func():
#   return lambda pair: pair[1]
# 调用：
pairs.sort(key=lambda pair: pair[1])
print(pairs)

#6. 文档字符串
def hello():
  '''Do nothing, but document it.

  No, really, it doesn't do anything.
  '''
  pass

print(hello.__doc__)

#7. 函数注解
def annotate(ham: 42, eggs: int = 'spam') -> "Nothing to see here":
  print("Annotations:", annotate.__annotations__)
  print("Arguments:", ham, eggs)

annotate('wonderful')