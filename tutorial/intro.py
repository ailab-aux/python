#!/usr/bin/env python3

# python tutorial
#  简介

# 这是一行注释，以`#`开头的即为注释，可以在行首，也可以在行中间
spam = 1 # 注释。

text = "#这不是一个注释，因为在引号中。"

# ====================== expression =========================
print("====================== expression =========================")

exp = 2 + 2
print("{0} + {1} = {2}".format(2, 2, exp))

#注意优先级，* 优于 -
exp = 50 - 5*6
print("{0} - {1}*{2} = {3}".format(50, 5, 6, exp))

#除法运算通常返回浮点数。
exp = (50 - 5*6) / 4
print("({0} - {1}*{2}) / {3} = {4}".format(50, 5, 6, 4, exp))

exp = 8 / 5
print("{0} / {1} = {2}".format(8, 5, exp))

#整数除法需要使用 `//` 运算符。
exp = 8 // 5
print("{0} // {1} = {2}".format(8, 5, exp))

#余数用 `%` 运算符
exp = 8 % 5
print("{0} % {1} = {2}".format(8, 5, exp))

#非整数也可以使用求余运算符
exp = 5.3 % 1.7
print("{0} % {1} = {2}".format(5.3, 1.7, exp))

#计算乘方 `**` 运算符
exp = 2 ** 4
print("{0} ** {1} = {2}".format(2, 4, exp))

exp = 3 ** 4
print("{0} ** {1} = {2}".format(3, 4, exp))

# ====================== string =========================
print("====================== string =========================")

#单引号
s = 'spam eggs'
print(s)

#单引号转义
s = 'doesn\'t'
print(s)

#双引号中间的单引号不需要转义
s = "doesn't"
print(s)

#单引号中的双引号
s = '"Yes," he said.'
print(s)

s = "\"Yes,\" he said."
print(s)

s = 'C:\some\name'
print(s)

#原始字符串，字符串内部所有字符都不转义 `r''`
s = r'C:\some\name'
print(s)
s = r"i'm a raw string\n"
print(s)

#多行字符串， `"""` 或者 `'''` 可以使用\防止当前行的行尾换行被包含进去。
s = """\
Usage: thingy [OPTIONS]
    -h          Display this usage message
    -H hostname Hostname to connect to\
"""
print(s)

#字符串可以用 + 表示连接字符串
a = "first string"
b = "second string"
s = a + b
print("{0} + {1} = {2}".format(a, b, s))

#字符串可以用 * 表示字符串重复多少次。
s = "string "
print('"{0}" * {1} = "{2}"'.format(s, 5, s * 5))

#当切分很长的字符串的时候可以使用 字符串自动连接功能: 'string a' 'string b'
text = ('i am a long long string, '
    'i have a long long long long long long string.')
print(text)

# ====================== string slice =========================
print('====================== string slice =========================')

# 索引 index 可以是正数也可以是负数，负数代表倒序。
###索引太大会导致错误。
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1
word = 'Python'
print('{0}[{1}]={2}, {0}[{3}]={4}'.format(word, 0, word[0], 5, word[5]))
print('{0}[-1]={1}, {0}[-2]={2}, {0}[-6]={3}'.format(word, word[-1], word[-2], word[-6]))

# 切片(slice) [first:second:step]
# word[x:] = word[x:len(word)]
# word[:y] = word[0:y]
# word[:] = word[0:len(word)] = [ 0, len(word) )
### 切片的结束太大不会错误，但是会截断。如 word[4:42] = work[4:len(word)] = word[4:6]
print('word[{0}:{1}]={2}'.format(4, 42, word[4:42]))

# 字符串特性： 字符串是不可变的，和C不同。
### 要修改字符串，需要新建一个字符串。
s = 'J' + word[1:]
print('{0} + {1} = {2}'.format('J', word[1:], s))

# 内置函数len()计算字符串的长度。
print('string `{0}`\'s length(len({0})) = {1}'.format(s, len(s)))

# ====================== list =========================
print('====================== list =========================')

# 列表，内部元素不必是同一类型。并且可以嵌套列表。
squares = [1, 4, 9, 16, 25]
print(squares)

wtf = [1, "hello", 2.5, [1, 'world']]
print(wtf)

# 列表支持切片，和字符串一样 [start:end:step]
print(squares[1:3])
print(wtf[1:3])

#列表支持连接操作 `+`
fuck = squares + wtf
print('{0} + {1} = {2}'.format(squares, wtf, fuck))

#列表内部的索引元素可以修改，可以修改单个索引，也可以修改一个范围：
fuck[-4:] = [36]
print(fuck)

# 可以清空 []
fuck[:] = []
print(fuck)

#内置函数len()同样适用于列表
squares = [1, 4, 9, 16, 25]
print('len({0}) = {1}'.format(squares, len(squares)))

wtf = [1, "hello", 2.5, [1, 'world']]
print('len({0}) = {1}'.format(wtf, len(wtf)))

# ====================== beginning =========================
print('====================== beginning =========================')

print("Fibonacci print......")
a, b = 0, 1
while b < 10:
  print(b)
  a, b = b, a + b

print("Fibonacci print......")
a, b = 0, 1
while b < 10:
  print(b, end=",")
  a, b = b, a + b
print('')