#!/usr/bin/env python3

# 内置数据类型， 列表/字典/等的循环获取元素。

#1. items()针对 字典。
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
  print(k, v)

#2. enumerate() 列表/序列
for i, v in enumerate(['tic', 'tac', 'toe']):
  print(i, v)