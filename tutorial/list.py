#!/usr/bin/env python3

# 数据结构

#1. list的操作
#.1 append(x) == a[len(a):] = [x]

a = [1, 2, 3]
a.append(4)
print(a)

a[len(a):] = [5]
print(a)

#.2 extend(L) = a[len(a):] = L
b = [1, 2, 3]
b.extend([4, 5, 6])
print(b)

b[len(b):] = [7, 8, 9]
print(b)

#.3 insert(i, x) 
c = [2, 3, 4]
c.insert(0, 1)
print(c)

#.4 remove(x), 只会删除第一个匹配的元素。
d = [1, 2, 3, 4, 4, 5]
d.remove(1)
print(d)
d.remove(4)
print(d) 

#.5 pop(i), pop()删除最后一个元素。
a = [1, 2, 3, 4]
b = a.pop(1)
print(a)
print(b)
b = a.pop()
print(a)
print(b)

#.6 clear() 删除所有元素。
a = [1, 2, 3, 4, 5]
a.clear()
print(a)
b = list(range(10))
b.clear()
print(b)

#.7 index(value) 第一个值对应的索引，如果没有匹配的元素会返回一个错误。
a = list(range(1, 10))
print("index =", a.index(9))
#下面的语句将报错。 ValueError
#a.index(10)

#.8 count(x) 列表中x出现的次数。
a = list(range(1, 10))
print("count[1] =", a.count(1))

#.9 sort() 对列表就地进行排序。
a = list(range(1, 10))
a.insert(0, 10)
print(a)
a.sort()
print(a)

#.10 reverse() 对列表进行倒排序。
a.reverse()
print(a)

#.11 copy() 返回列表的一个浅拷贝。等价于 a[:],拷贝后两者互不相干。
b = a.copy()
b[2] = 18
a[9] = 19
print(a)
print(b)

#2. 把列表当做堆栈使用。
def list_as_stack():
  stack = [3, 4, 5]
  # push.
  stack.append(6)
  stack.append(7)
  print(stack)
  print('pop stack =', stack.pop())
  print('pop stack =', stack.pop())
  print('pop stack =', stack.pop())
  print('pop stack =', stack.pop())
  print(stack)

list_as_stack()

#3. 把列表当做队列使用。
# 通常都在列表的尾部进行添加和弹出。所以通常使用collections.deque 双端队列来实现队列

from collections import deque

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

#4. 列表推导式。
# 
def make_squares(max = 10):
  out = []
  for x in range(max):
    out.append(x ** 2)
  return out

print(make_squares())

# map()函数在python3.x返回一个迭代器，参数为(func, iterable, ...), func作用于iterable上的每一个元素。
squares = list(map(lambda x: x ** 2, range(10)))
print(squares)

# 列表推导式：
# 列表推导式由包含一个表达式的括号组成，
# 表达式后面跟随一个 for 子句，之后可以有零或多个 for 或 if 子句。
# 结果是一个列表，由表达式依据其后面的 for 和 if 子句上下文计算而来的结果构成
squares = [x ** 2 for x in range(10)]
print(squares)

hi = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(hi)
# 等价于
hi = []
for x in [1, 2, 3]:
  for y in [3, 1, 4]:
    if x != y:
      hi.append((x, y))
print(hi)

# 列表推导式。
vec = [-4, -2, 0, 2, 4]
print([x * 2 for x in vec])
print([x for x in vec if x >= 0])
print([abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# strip()函数用于删除字符串的开头和结尾的特定字符，如果没有参数，则默认删除空白字符。`\n\r\t `
print([weapon.strip() for weapon in freshfruit])

print([(x, x**2) for x in range(6)])
#下面的语句导致错误。如果需要元组，需要添加括号。
#print([x, x**2 for x in range(6)])

# 有意思
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])

# 复杂的推导式和嵌套函数
from math import pi
print([str(round(pi, i)) for i in range(1, 6)])

#4. 嵌套的列表推导式

#转置矩阵
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]

print([[row[i] for row in matrix] for i in range(4)])
#等价于
hi = []
for i in range(4):
  hi.append([row[i] for row in matrix])
print(hi)
#等价于
hi = []
for i in range(4):
  row = []
  for r in matrix:
    row.append(r[i])
  hi.append(row)
print(hi)

print(matrix)
# 可以使用内置的zip()函数进行转置
print(list(zip(*matrix)))