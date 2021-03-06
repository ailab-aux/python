#!/usr/bin/env python3

# 序列比较 
# 比较操作按 字典序 进行：
#   首先比较前两个元素，如果不同，就决定了比较的结果；
#   如果相同，就比较后两个元素，依此类推，直到所有序列都完成比较。
#   如果两个元素本身就是同样类型的序列，就递归字典序比较。
#   如果两个序列的所有子项都相等，就认为序列相等。
#   如果一个序列是另一个序列的初始子序列，较短的一个序列就小于另一个。
#   字符串的字典序按照单字符的 ASCII 顺序

x = (1, 2, 3)
y = (1, 2, 4)
print(x, y, x < y)

a = 'ABC'
b = 'C'
c = 'Pascal'
d = 'Python'
print(a, b, c, d, a < b < c < d)

x = (1, 2, 3, 4)
y = (1, 2, 4)
print(x, y, x < y)

x = (1, 2)
y = (1, 2, -1)
print(x, y, x < y)

# 需要注意的是如果通过 < 或者 > 比较的对象只要具有合适的比较方法就是合法的。
# 比如，混合数值类型是通过它们的数值进行比较的，所以 0 是等于 0.0 。
# 否则解释器将会触发一个 TypeError 异常，而不是提供一个随意的结果。

x = (1, 2, 3)
y = (1.0, 2.0, 3.0)
print(x, y, x == y)

x = (1, 2, ('aa', 'bb'))
y = (1, 2, ('abc', 'a'), 4)
print(x, y, x < y)