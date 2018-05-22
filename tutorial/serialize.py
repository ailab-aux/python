#!/usr/bin/env python3

# json序列化/反序列化 数据

# 标准模块 json 可以接受 Python 数据结构，并将它们转换为字符串表示形式；此过程称为 序列化。
# 从字符串表示形式重新构建数据结构称为 反序列化。
# 序列化和反序列化的过程中，表示该对象的字符串可以存储在文件或数据中，也可以通过网络连接传送给远程的机器。

import json

# dumps() 函数的另外一个变体 dump()，直接将对象序列化到一个文件。所以如果 f 是为写入而打开的一个 文件对象，我们可以这样做:

print(json.dumps([1, 'simple', 'list']))

fname = 'data.bin'
with open(fname, 'w') as f:
  x = [1, 'simple', 'list']
  json.dump(x, f)

# 为了重新解码对象，如果 f 是为读取而打开的 文件对象:

with open(fname, 'r') as f:
  x = json.load(f)
  print(x)