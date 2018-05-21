#!/usr/bin/env python3

# 字典 dict key/value 集合
# key必须式不可变类型，如字符串，数值和元组，元组（但是要求元组内部不能有可变类型（列表等））。
# key必须式各不相同的。
# {}创建一个空字典。
# 大括号内的key/value对的格式为 key: value, ...
# 可以通过key来存储或获取值
# 可以通过del来删除key/value对。
# 向已经存在的key中存储数值，将覆盖原来的数据。
# 从一个不存在的key中取值，将导致错误。
# list(d.keys())将获取字典中所有关键字组成的无序列表。
# 可以用sorted(d.keys())对关键字进行排序。
# 可以使用in关键字查询字典中是否存在某个关键字

tel = {'jack': 4098, 'sape': 4139}
print(tel)

# 添加key/value对。
tel['guido'] = 4127
print(tel)

# 已有，覆盖。
tel['jack'] = 10000
print(tel)

# 获取对应的key的value
print(tel['jack'])

# 删除key/value对
del tel['sape']
print(tel)

tel['irv'] = 4127

#取key
print(list(tel.keys()))

#对key排序
print(sorted(tel.keys()))

#判断key是否在集合内
print('guido' in tel)
print('jack' not in tel)

# dict()函数通过key/value对 创建字典
d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(d)
# 如果关键字都是字符串，则可以使用key-value对更加方便。
d = dict(sape=4139, guido=4127, jack=4098)
print(d)

# 字典推导式。
hi = {x: x**2 for x in (2, 4, 6)}
print(hi)
