#!/usr/bin/env python3

# 文件读写

#1. 打开
#
# 函数 open() 返回 文件对象，通常的用法需要两个参数：open(filename, mode)。
# mode 为 'r' 时表示只是读取文件；
# 'w' 表示只是写入文件（已经存在的同名文件将被删掉）；
# 'a' 表示打开文件进行追加，写入到文件中的任何数据将自动添加到末尾。 
# 'r+' 表示打开文件进行读取和写入。mode 参数是可选的，默认为 'r'。
#
# 通常，文件以 文本 打开，这意味着，你从文件读出和向文件写入的字符串会被特定的编码方式（默认是UTF-8）编码。
# 模式后面的 'b' 以 二进制模式 打开文件：数据会以字节对象的形式读出和写入。这种模式应该用于所有不包含文本的文件。
#
# 在文本模式下，读取时默认会将平台有关的行结束符（Unix上是 \n , Windows上是 \r\n）转换为 \n。
# 在文本模式下写入时，默认会将出现的 \n 转换成平台有关的行结束符。
# 这种暗地里的修改对 ASCII 文本文件没有问题，但会损坏 JPEG 或 EXE 这样的二进制文件中的数据。使用二进制模式读写此类文件时要特别小心。

print(__file__)
f = open(__file__, 'r')

#2. 读取
#
# 该方法读取若干数量的数据并以字符串形式返回其内容，size 是可选的数值，指定字符串长度。
# 如果没有指定 size 或者指定为负数，就会读取并返回整个文件。
# 当文件大小为当前机器内存两倍时，就会产生问题。反之，会尽可能按比较大的 size 读取和返回数据。
# 如果到了文件末尾，f.read() 会返回一个空字符串（''）:

#print(f.read())
#print(f.read())

# f.readline() 从文件中读取单独一行，字符串结尾会自动加上一个换行符（ \n ），
# 只有当文件最后一行没有以换行符结尾时，这一操作才会被忽略。
# 这样返回值就不会有混淆，如果 f.readline() 返回一个空字符串，
# 那就表示到达了文件末尾，如果是一个空行，就会描述为 '\n'，一个只包含换行符的字符串:

while True:
  line = f.readline()
  if line is '':
    break
  print(line, end=' ')

f.seek(0)
# 你可以循环遍历文件对象来读取文件中的每一行。这是一种内存高效、快速，并且代码简介的方式:
for line in f:
  print(line, end=' ')

f.seek(0)
# 如果你想把文件中的所有行读到一个列表中，你也可以使用 list(f) 或者 f.readlines()。
lines = list(f)
lines = f.readlines()
f.close()

#3. 写入文件。
#
# f.write(string) 方法将 string 的内容写入文件，并返回写入字符的长度:

fname = __file__ + 'd'
f = open(fname, 'w')
f.write('I am a file of ' + fname)

# 想要写入其他非字符串内容，首先要将它转换为字符串:

value = ('the answer', 42)
s = str(value)
f.write(s)

#4. 文件位置
#
# f.tell() 返回一个整数，代表文件对象在文件中的指针位置，该数值计量了自文件开头到指针处的比特数。
# 需要改变文件对象指针话话，使用 f.seek(offset,from_what)。
# 指针在该操作中从指定的引用位置移动 offset 比特，引用位置由 from_what 参数指定。 
# from_what 值为 0 表示自文件起始处开始，1 表示自当前文件指针位置开始，2 表示自文件末尾开始。from_what 可以忽略，其默认值为零，此时从文件头开始:
#
# 在文本文件中（没有以 b 模式打开），只允许从文件头开始寻找（有个例外是用 seek(0, 2) 寻找文件的最末尾处）而且合法的 偏移 值只能是 f.tell() 返回的值或者是零。
# 其它任何 偏移 值都会产生未定义的行为。

fr = open(__file__, "r")
for line in fr:
  f.write(line)
f.close()
fr.close()

f = open('test.bin', 'wb+')
f.write(b'0123456789abcdef')

l = f.tell()
print(f.tell())
print(f.seek(5))

f.seek(l)
f.seek(-3, 2)
print(f.read(1))

f.close()

# 用关键字 with 处理文件对象是个好习惯。它的先进之处在于文件用完后会自动关闭，就算发生异常也没关系。它是 try-finally 块的简写:

with open(__file__, 'r') as f:
  f.read()

print(f.closed)