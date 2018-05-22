#!/usr/bin/env python3

# 包
# 包通常是使用用“圆点模块名”的结构化模块命名空间。例如，名为 A.B 的模块表示了名为 A 的包中名为 B 的子模块。
#  正如同用模块来保存不同的模块架构可以避免全局变量之间的相互冲突，
#  使用圆点模块名保存像 NumPy 或 Python Imaging Library 之类的不同类库架构可以避免模块之间的命名冲突。

# 当导入这个包时，Python 通过 sys.path 搜索路径查找包含这个包的子目录。
#   为了让 Python 将目录当做内容包，目录中必须包含 __init__.py 文件。
#   这是为了避免一个含有烂俗名字的目录无意中隐藏了稍后在模块搜索路径中出现的有效模块，比如 string。
#   最简单的情况下，只需要一个空的 __init__.py 文件即可。
#   当然它也可以执行包的初始化代码，或者定义稍后介绍的 __all__ 变量。

# .1
# 用户可以每次只导入包里的特定模块，例如:
# import sound.effects.echo
#这样就导入了 sound.effects.echo 子模块。它必需通过完整的名称来引用:
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# .2
# 导入包时有一个可以选择的方式:
# from sound.effects import echo
# 这样就加载了 echo 子模块，并且使得它在没有包前缀的情况下也可以使用，所以它可以如下方式调用:
# echo.echofilter(input, output, delay=0.7, atten=4)

# .3
# 还有另一种变体用于直接导入函数或变量:
# from sound.effects.echo import echofilter
# 这样就又一次加载了 echo 子模块，但这样就可以直接调用它的 echofilter() 函数:
# echofilter(input, output, delay=0.7, atten=4)

#WARNING:
# 需要注意的是使用 from package import item 方式导入包时，这个子项（item）既可以是包中的一个子模块（或一个子包），
# 也可以是包中定义的其它命名，像函数、类或变量。import 语句首先核对是否包中有这个子项，
# 如果没有，它假定这是一个模块，并尝试加载它。如果没有找到它，会引发一个 ImportError 异常。

# 1. 从 * 导入包
# 那么当用户写下 from sound.effects import * 时会发生什么事？
# 理想中，总是希望在文件系统中找出包中所有的子模块，然后导入它们。
# 这可能会花掉很长时间，并且出现期待之外的边界效应，导出了希望只能显式导入的包。

# 对于包的作者来说唯一的解决方案就是给提供一个明确的包索引。
# import 语句按如下条件进行转换：执行 from package import * 时，
# 如果包中的 __init__.py 代码定义了一个名为 __all__ 的列表，就会按照列表中给出的模块名进行导入。
# 新版本的包发布时作者可以任意更新这个列表。
# 如果包作者不想 import * 的时候导入他们的包中所有模块，那么也可能会决定不支持它（ import * ）。
# 例如， sound/effects/__init__.py 这个文件可能包括如下代码:
# __all__ = ["echo", "surround", "reverse"]
#
# 这意味着 from sound.effects import * 语句会从 sound 包中导入以上三个已命名的子模块。
# 如果没有定义 __all__ ， from sound.effects import * 语句 不会 从 sound.effects 包中导入所有的子模块。
# 无论包中定义多少命名，只能确定的是导入了 sound.effects 包（可能会运行 __init__.py 中的初始化代码）以及包中定义的所有命名会随之导入。
# 这样就从 __init__.py 中导入了每一个命名（以及明确导入的子模块）。
# 同样也包括了前述的 import 语句从包中明确导入的子模块，考虑以下代码:
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *
# 
# 尽管某些模块设计为使用 import * 时它只导出符合某种规范/模式的命名，仍然不建议在生产代码中使用这种写法。
# 记住，from Package import specific_submodule 没有错误！事实上，除非导入的模块需要使用其它包中的同名子模块，否则这是推荐的写法。

# 2. 包内引用
# 如果包中使用了子包结构（就像示例中的 sound 包），可以按绝对位置从相邻的包中引入子模块。
# 例如，如果 sound.filters.vocoder 包需要使用 sound.effects 包中的 echo 模块，它可以 from sound.Effects import echo。
# 
# 你可以用这样的形式 from module import name 来写显式的相对位置导入。
# 那些显式相对导入用点号标明关联导入当前和上级包。以 surround 模块为例，你可以这样用:
# 
# from . import echo
# from .. import formats
# from ..filters import equalizer
# 
# 需要注意的是显式或隐式相对位置导入都基于当前模块的命名。
# 因为主模块的名字总是 "__main__"，Python 应用程序的主模块应该总是用绝对导入。
#

# 3. 多重目录中的包
# 包支持一个更为特殊的特性， __path__。 
# 在包的 __init__.py 文件代码执行之前，该变量初始化一个目录名列表。该变量可以修改，它作用于包中的子包和模块的搜索功能。
# 这个功能可以用于扩展包中的模块集，不过它不常用。