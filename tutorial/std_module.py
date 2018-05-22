#!/usr/bin/env python3

# 标准模块

# Python 带有一个标准模块库，并发布有独立的文档，名为 Python 库参考手册（此后称其为“库参考手册”）。
# 有一些模块内置于解释器之中，这些操作的访问接口不是语言内核的一部分，但是已经内置于解释器了。
# 这既是为了提高效率，也是为了给系统调用等操作系统原生访问提供接口。
# 这类模块集合是一个依赖于底层平台的配置选项。
#   例如，winreg 模块只提供在 Windows 系统上才有。
#   有一个具体的模块值得注意： sys ，这个模块内置于所有的 Python 解释器。
#   变量 sys.ps1 和 sys.ps2 定义了主提示符和辅助提示符字符串:

import sys

#只在交互模式下面才有意义，如果不是交互模式下，则没有，会报错。
# print(sys.ps1)
# print(sys.ps2)
print(sys.path)
for i, v in enumerate(sys.path):
  print(v)