#!/usr/bin/env python3

# for statement
# for语句

words = ['cat', 'window', 'defenestrate']
for w in words:
  print(w, len(w))

# for循环中修改迭代器通常不是一个好的编程方式
# 通常可以使用列表的副本： list[:]即产生一个副本。

for w in words[:]:
  if len(w) > 6:
    words.insert(0, w)

print(words)

#注意上面的例子中words[:]产生了一个副本。