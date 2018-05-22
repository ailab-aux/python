#!/usr/bin/env python3

# 输入/输出

# string类 format()方法， Template方法
# repr()/str()函数
# 

s = 'Hello, world.'
print(str(s))
print(repr(s))

print(str(1/7))

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)

hi = 'hello, world\n'
his = repr(hi)
print(his)

print(repr((x, y, ('spam', 'eggs'))))

# str.rjust()right对齐。左侧填充空格使之右对齐。
# 类似的方法还有 str.ljust() 和 str.center()。
# 这些函数只是输出新的字符串，并不改变什么。
# 如果输出的字符串太长，它们也不会截断它，而是原样输出，这会使你的输出格式变得混乱，不过总强过另一种选择（截断字符串），因为那样会产生错误的输出值
# （如果你确实需要截断它，可以使用切割操作，例如：x.ljust(n)[:n] ）。
# 还有另一个方法， str.zfill() 它用于向数值的字符串表达左侧填充 0。该函数可以正确理解正负号:
for x in range(1, 11):
  print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
  print(repr(x*x*x).rjust(4))

for x in range(1, 11):
  print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# str.zfill() 可以知道正负数，并正确填充零。
print('12'.zfill(5))              # 00012
print('-3.14'.zfill(7))           # -003.14
print('3.14159265359'.zfill(5))   # 3.14159265359

# str.format()基本用法
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# 如果在 str.format() 调用时使用关键字参数，可以通过参数名来引用值:
print('This {food} is {adjective}.'.format(
  food='spam', adjective='absolutely horrible'
))

#位置参数和关键字参数可以随意组合:
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# '!a' (应用 ascii())，'!s' （应用 str() ）和 '!r' （应用 repr() ）可以在格式化之前转换值:
import math
print('The value of Pi is approximately {}.'.format(math.pi))
print('The value of PI is approximately {!r}.'.format(math.pi))

# 字段名后允许可选的 ':' 和格式指令。这允许对值的格式化加以更深入的控制。下例将 Pi 转为三位精度。
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

# 在字段后的 ':' 后面加一个整数会限定该字段的最小宽度，这在美化表格时很有用:
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
  print('{0:10} ==> {1:10}'.format(name, phone))

# 如果你有个实在是很长的格式化字符串，不想分割它。
# 如果你可以用命名来引用被格式化的变量而不是位置就好了。
# 有个简单的方法，可以传入一个字典，用中括号( '[]' )访问它的键:
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# 也可以用 ‘**’ 标志将这个字典以关键字参数的方式传入:
print('Jack: {Jack:d}; Sjoerd:{Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# 旧式的字符串格式化
print('The value of PI is approximately %5.3f.' % math.pi)