#!/usr/bin/env python3

# 生成器

# Generator 是创建迭代器的简单而强大的工具。它们写起来就像是正规的函数，需要返回数据的时候使用 yield 语句。
# 每次 next() 被调用时，生成器回复它脱离的位置（它记忆语句最后一次执行的位置和所有的数据值）。以下示例演示了生成器可以很简单的创建出来:

def reverse(data):
  print("hello")
  for index in range(len(data) - 1, -1, -1):
    print("index =", index)
    yield data[index]
  print("world")

for char in reverse('golf'):
  print(char, end="")
print()

# 生成器表达式

# 有时简单的生成器可以用简洁的方式调用，就像不带中括号的链表推导式。
# 这些表达式是为函数调用生成器而设计的。生成器表达式比完整的生成器定义更简洁，但是没有那么多变，而且通常比等价的链表推导式更容易记。
#

print(sum(i * i for i in range(10)))
xv = [10, 20, 30]
yv = [7, 5, 3]
print(sum(x*y for x, y in zip(xv, yv)))

from math import pi, sin
sin_table = {x: sin(x*pi/180) for x in range(0, 91)}

for k, v in sin_table.items():
  print('{0:2d} {1}'.format(k, v))

data = 'golf'
print(list(data[i] for i in range(len(data) - 1, -1, -1)))
