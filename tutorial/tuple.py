#!/usr/bin/env python3

# 元组 `x,y,z`
t = 12345, 54321, 'hello!'
print(t)
print(t[0])

#1. 元组可以嵌套
u = t, (1, 2, 3, 4, 5)
print(u)

#2. 元组内的元素不可修改，和字符串相同。
# 但是可以包含可修改的对象。
# 其中的列表即为可修改对象。
v = ([1, 2, 3], [3, 2, 1])

#3. 元组输出式总是带括号，输入可以有也可以没有。
#4. 单个值的元组，通常为了防止混淆，在单个值后面添加逗号，丑陋，但是有效 WTF？？？
x = (10,)
print(x)

empty = ()
print(empty)
print(len(empty))

# 这样写很有意思，难道不怕产生歧义吗？丑陋。。。WTF？？？
singleton = 'hello',
print(singleton)
print(len(singleton))

#5. 元组可以进行逆操作
# 语句 t = 12345, 54321, 'hello!' 是 元组封装 （tuple packing）
# 这个调用等号右边可以是任何线性序列，称之为 序列拆封 非常恰当
# 要注意的是可变参数（multiple assignment ）其实只是元组封装和序列拆封的一个结合。
x, y, z = t
print(x, y, z)


