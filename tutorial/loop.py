#!/usr/bin/env python3

# 内置数据类型， 列表/字典/等的循环获取元素。

#1. items()针对 字典。
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k, v)

#2. enumerate() 列表/序列
for i, v in enumerate(['tic', 'tac', 'toe']):
  print(i, v)

#3. zip()整体打包
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
  print('What is you {0}? It is {1}.'.format(q, a))

#4. reversed()倒序
for i in reversed(range(1, 10, 2)):
  print(i, end=' ')
print("")

#5. sorted() 函数不改变原来的序列，而是重新生成一个新的有序的序列并返回。
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
  print(f, end=',')
print('')

#6. 使用切片获取序列副本。
words = ['cat', 'window', 'defenestrate']
for w in words[:]: #only create the copy of words.
  if len(w) > 6:
    words.insert(0, w)
print(words)