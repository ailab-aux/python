#!/usr/bin/env python3

# 迭代器

# 现在你可能注意到大多数容器对象都可以用 for 遍历:

for element in [1, 2, 3]:
  print(element)
for e in (1, 2, 3):
  print(e)
for key in {'one': 1, 'two': 2}:
  print(key)
for char in "123":
  print(char)
for line in open(__file__):
  print(line, end=' ')

# 这种形式的访问清晰、简洁、方便。迭代器的用法在 Python 中普遍而且统一。
#   在后台， for 语句在容器对象中调用 iter() 。
#   该函数返回一个定义了 __next__() 方法的迭代器对象，它在容器中逐一访问元素。
#   没有后续的元素时， __next__() 抛出一个 StopIteration 异常通知 for 语句循环结束。
#   你可以是用内建的 next() 函数调用 __next__() 方法；以下是其工作原理的示例:

s = 'abc'
it = iter(s)
print(it)
print(next(it))
print(next(it))
print(next(it))
try:
  print(next(it))
except StopIteration as e:
  print("stop iteration error:", e)

# 了解了迭代器协议的后台机制，就可以很容易的给自己的类添加迭代器行为。
#   1. 定义一个 __iter__() 方法，使其返回一个带有 __next__() 方法的对象。
#   2. 如果这个类已经定义了 __next__() ，那么 __iter__() 只需要返回 self:

class Reverse:
  """Iterator for looping over a sequence backwards."""
  def __init__(self, data):
    self.data = data
    self.index = len(data)
  def __iter__(self):
    return self
  def __next__(self):
    if self.index == 0:
      raise StopIteration
    self.index = self.index - 1
    return self.data[self.index]

rev = Reverse('Hello, world!')
print(iter(rev))
for c in rev:
  print(c, end='')
print()