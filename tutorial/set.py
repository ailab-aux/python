#!/usr/bin/env python3

# 集合
# 集合是一个无序不重复元素的集
# 基本功能包括关系测试和消除重复元素。
# 集合对象还支持 union（联合），intersection（交），difference（差）和 sysmmetric difference（对称差集）等数学运算。
# {} 和 set()函数可以创建集合。
# 要想创建空集合， 必须使用set()函数。{}用于创建空字典。
# 

# 重复元素自动删除
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# 集合元素查找
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a)

#集合的运算， 差/并/交/？ in a or in b， but all in
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

#集合推导式
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)