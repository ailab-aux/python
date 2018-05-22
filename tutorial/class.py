#!/usr/bin/env python3

# 类
#
# 类的大多数重要特性都被完整的保留下来：
#   1. 类继承机制允许多重继承，
#   2. 派生类可以覆盖（override）基类中的任何方法或类，
#   3. 可以使用相同的方法名称调用基类的方法。
#   4. 对象可以包含任意数量的私有数据。

'''
命名空间 是从命名到对象的映射。当前命名空间主要是通过 Python 字典实现的，不过通常不关心具体的实现方式（除非出于性能考虑），以后也有可能会改变其实现方式。
以下有一些命名空间的例子：内置命名（像 abs() 这样的函数，以及内置异常名）集，模块中的全局命名，函数调用中的局部命名。
某种意义上讲对象的属性集也是一个命名空间。
关于命名空间需要了解的一件很重要的事就是不同命名空间中的命名没有任何联系，例如两个不同的模块可能都会定义一个名为 maximize 的函数而不会发生混淆－用户必须以模块名为前缀来引用它们。

顺便提一句，我称 Python 中任何一个“.”之后的命名为 属性
－－例如，表达式 z.real 中的 real 是对象 z 的一个属性。
严格来讲，从模块中引用命名是引用属性：表达式 modname.funcname 中，modname 是一个模块对象，funcname 是它的一个属性。
因此，模块的属性和模块中的全局命名有直接的映射关系：它们共享同一命名空间！[1]

属性可以是只读过或写的。后一种情况下，可以对属性赋值。你可以这样作： modname.the_answer = 42 。
可写的属性也可以用 del 语句删除。例如： del modname.the_answer 会从 modname 对象中删除 the_answer 属性。

不同的命名空间在不同的时刻创建，有不同的生存期。
包含内置命名的命名空间在 Python 解释器启动时创建，会一直保留，不被删除。
模块的全局命名空间在模块定义被读入时创建，通常，模块命名空间也会一直保存到解释器退出。
由解释器在最高层调用执行的语句，不管它是从脚本文件中读入还是来自交互式输入，都是 __main__ 模块的一部分，
所以它们也拥有自己的命名空间（内置命名也同样被包含在一个模块中，它被称作 builtins ）。

当调用函数时，就会为它创建一个局部命名空间，并且在函数返回或抛出一个并没有在函数内部处理的异常时被删除。
（实际上，用遗忘来形容到底发生了什么更为贴切。）当然，每个递归调用都有自己的局部命名空间。



如果一个命名声明为全局的，那么对它的所有引用和赋值会直接搜索包含这个模块全局命名的作用域。如果要重新绑定最里层作用域之外的变量，可以使用 nonlocal 语句；
如果不声明为 nonlocal，这些变量将是只读的（对这样的变量赋值会在最里面的作用域创建一个新的局部变量，外部具有相同命名的那个变量不会改变）。

Python 的一个特别之处在于：如果没有使用 global 语法，其赋值操作总是在最里层的作用域。
赋值不会复制数据，只是将命名绑定到对象。删除也是如此：del x 只是从局部作用域的命名空间中删除命名 x 。
事实上，所有引入新命名的操作都作用于局部作用域。特别是 import 语句和函数定义将模块名或函数绑定于局部作用域（可以使用 global 语句将变量引入到全局作用域）。

global 语句用以指明某个特定的变量为全局作用域，并重新绑定它。nonlocal 语句用以指明某个特定的变量为封闭作用域，并重新绑定它。

'''

def scope_test():
  def do_local():
    spam = "local spam"
  def do_nonlocal():
    nonlocal spam
    spam = "nonlocal spam"
  def do_global():
    global spam
    spam = "global spam"
  spam = "test spam"
  #修改了局部的变量，并不影响外围的变量
  do_local()
  print("After local assignment:", spam)
  #修改了do_nonlocal()函数内部作用域外层的变量
  do_nonlocal()
  print("After nonlocal assignment:", spam)
  #全局变量spam的新创建。
  do_global()
  print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

i = 0

def a():
  global i
  i = 1
  print('local:', i)

a()
print('global:', i)

#3.
#.1 类定义语法
# 作用域：
#  进入类定义部分后，会创建出一个新的命名空间，作为局部作用域。因此，所有的赋值成为这个新命名空间的局部变量。特别是函数定义在此绑定了新的命名。
# 类对象：
#  类定义完成时（正常退出），就创建了一个 类对象。基本上它是对类定义创建的命名空间进行了一个包装；

#.2 类对象
# 类对象支持两种操作：
#   1. 属性引用
#   2. 实例化
# 
class MyClass:
  """A simple example class"""
  i = 12345
  def f(self):
    return 'hello world'

#属性引用：
#
# 那么 MyClass.i 和 MyClass.f 是有效的属性引用，分别返回一个整数和一个方法对象。
# 也可以对类属性赋值，你可以通过给 MyClass.i 赋值来修改它。 
# __doc__ 也是一个有效的属性，返回类的文档字符串："A simple example class"。
#WARNING: 感觉可以理解为类的静态属性。而不是实例属性。

#实例化：
#
# 类的 实例化 使用函数符号。只要将类对象看作是一个返回新的类实例的无参数函数即可。例如（假设沿用前面的类）:
x = MyClass()
# 以上创建了一个新的类 实例 并将该对象赋给局部变量 x。
#
# 这个实例化操作（“调用”一个类对象）来创建一个空的对象。很多类都倾向于将对象创建为有初始状态的。因此类可能会定义一个名为 __init__() 的特殊方法，像下面这样:
# def __init__(self):
#   self.data = []
#
# 类定义了 __init__() 方法的话，类的实例化操作会自动为新创建的类实例调用 __init__() 方法。所以在下例中，可以这样创建一个新的实例:
# x = MyClass()
#
# 当然，出于弹性的需要，__init__() 方法可以有参数。事实上，参数通过 __init__() 传递到类的实例化操作上。例如，

class Complex:
  def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart

c = Complex(3.0, -4.5)
print(c.r, c.i)

#.3 实例对象
# 现在我们可以用实例对象作什么？实例对象唯一可用的操作就是属性引用。有两种有效的属性名。
#   1. 数据属性
#   2. 方法属性

# 实例对象的有效名称依赖于它的类。
# 按照定义，类中所有（用户定义）的函数对象对应它的实例中的方法。
# 所以在我们的例子中，x.f 是一个有效的方法引用，因为 MyClass.f 是一个函数。但 x.i 不是，因为 MyClass.i 不是函数。
# 不过 x.f 和 MyClass.f 不同，它是一个 方法对象 ，不是一个函数对象。

#.4 方法对象
# 
# x.f()
# 在 MyClass 示例中，这会返回字符串 'hello world'。然而，也不是一定要直接调用方法。 x.f 是一个方法对象，它可以存储起来以后调用。例如:
#
xf = x.f
print(xf())

# 实际上，你可能已经猜到了答案：方法的特别之处在于实例对象作为函数的第一个参数传给了函数。
# 在我们的例子中，调用 x.f() 相当于 MyClass.f(x) 。通常，以 n 个参数的列表去调用一个方法就相当于将方法的对象插入到参数列表的最前面后，以这个列表去调用相应的函数。
#
# 如果你还是不理解方法的工作原理，了解一下它的实现也许有帮助。引用非数据属性的实例属性时，会搜索它的类。
# 如果这个命名确认为一个有效的函数对象类属性，就会将实例对象和函数对象封装进一个抽象对象：这就是方法对象。
# 以一个参数列表调用方法对象时，它被重新拆封，用实例对象和原始的参数列表构造一个新的参数列表，然后函数对象调用这个新的参数列表。

#.5 类和实例变量
# 类似于类的静态成员和实例成员

class Dog:
  kind = 'canine'
  def __init__(self, name):
    self.name = name

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)
print(e.kind)
print(d.name)
print(e.name)

#WARNING: 正如在 术语相关 讨论的， 可变 对象，例如列表和字典，的共享数据可能带来意外的效果。
# 例如，下面代码中的 tricks 列表不应该用作类变量，因为所有的 Dog 实例将共享同一个列表:

class Dog2:
  tricks = []
  def __init__(self, name):
    self.name = name
  def add_trick(self, trick):
    self.tricks.append(trick)

d = Dog2('Fido')
e = Dog2('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)

# 你可以设计为类的实例变量
class Dog3:
  def __init__(self, name):
    self.name = name
    self.tricks = []
  def add_trick(self, trick):
    self.tricks.append(trick)

d = Dog3('Fido')
e = Dog3('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)

#4. 说明
#
# 数据属性会覆盖同名的方法属性。为了避免意外的名称冲突，这在大型程序中是极难发现的 Bug，使用一些约定来减少冲突的机会是明智的。
# 可能的约定包括：大写方法名称的首字母，使用一个唯一的小字符串（也许只是一个下划线）作为数据属性名称的前缀，或者方法使用动词而数据属性使用名词。
#
# 数据属性可以被方法引用，也可以由一个对象的普通用户（客户）使用。换句话说，类不能用来实现纯净的数据类型。
# 事实上，Python 中不可能强制隐藏数据——一切基于约定（如果需要，使用 C 编写的 Python 实现可以完全隐藏实现细节并控制对象的访问。这可以用来通过 C 语言扩展 Python）。
#
# 客户应该谨慎的使用数据属性——客户可能通过践踏他们的数据属性而使那些由方法维护的常量变得混乱。
# 注意：只要能避免冲突，客户可以向一个实例对象添加他们自己的数据属性，而不会影响方法的正确性——再次强调，命名约定可以避免很多麻烦。
#
# 一般，方法的第一个参数被命名为 self。这仅仅是一个约定：对 Python 而言，名称 self 绝对没有任何特殊含义。
# （但是请注意：如果不遵循这个约定，对其他的 Python 程序员而言你的代码可读性就会变差，而且有些 类查看器 程序也可能是遵循此约定编写的。）
# 
# 类属性的任何函数对象都为那个类的实例定义了一个方法。函数定义代码不一定非得定义在类中：也可以将一个函数对象赋值给类中的一个局部变量。例如:

def f1(self, x, y):
  return min(x, x+y)
class C:
  f = f1
  def g(self):
    return 'hello, world'
  h = g
# 上述的做法并不推荐：
# 现在 f， g 和 h 都是类 C 的属性，引用的都是函数对象，因此它们都是 C 实例的方法－－ h 严格等于 g 。要注意的是这种习惯通常只会迷惑程序的读者。
#
# 通过 self 参数的方法属性，方法可以调用其它的方法:
class Bag:
  def __init__(self):
    self.data = []
  def add(self, x):
    self.data.append(x)
  def addtwice(self, x):
    self.add(x)
    self.add(x)

# 
# 方法可以像引用普通的函数那样引用全局命名。与方法关联的全局作用域是包含类定义的模块。（类本身永远不会做为全局作用域使用。）
# 尽管很少有好的理由在方法 中使用全局数据，全局作用域确有很多合法的用途：其一是方法可以调用导入全局作用域的函数和方法，也可以调用定义在其中的类和函数。
# 通常，包含此方法的类也会定义在这个全局作用域，在下一节我们会了解为何一个方法要引用自己的类。
#
#  每个值都是一个对象，因此每个值都有一个 类( class ) （也称为它的 类型( type ) ），它存储为 

#5. 继承
# 
# class DerivedClass(BaseClass):
#   ...
# 命名 BaseClassName （示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
# class DerivedClass(modname.BaseClass):
#   ...
# 
# 派生类定义的执行过程和基类是一样的。构造派生类对象时，就记住了基类。这在解析属性引用的时候尤其有用：
#   如果在类中找不到请求调用的属性，就搜索基类。
#   如果基类是由别的类派生而来，这个规则会递归的应用上去。
#
# 派生类的实例化没有什么特殊之处： DerivedClass() （示列中的派生类）创建一个新的类实例。
# 方法引用按如下规则解析：搜索对应的类属性，必要时沿基类链逐级搜索，如果找到了函数对象这个方法引用就是合法的。
#
# 派生类可能会覆盖其基类的方法。因为方法调用同一个对象中的其它方法时没有特权，基类的方法调用同一个基类的方法时，可能实际上最终调用了派生类中的覆盖方法。
# （对于 C++ 程序员来说，Python 中的所有方法本质上都是 虚 方法。）
#
# 派生类中的覆盖方法可能是想要扩充而不是简单的替代基类中的重名方法。有一个简单的方法可以直接调用基类方法，
#   只要调用： BaseClassName.methodname(self, arguments)。有时这对于客户也很有用。（要注意只有 BaseClassName 在同一全局作用域定义或导入时才能这样用。）
#
# Python 有两个用于继承的函数：
#   1. 函数 isinstance() 用于检查实例类型： isinstance(obj, int) 只有在 obj.__class__ 是 int 或其它从 int 继承的类型
#   2. 函数 issubclass() 用于检查类继承： issubclass(bool, int) 为 True，因为 bool 是 int 的子类。
#      然而， issubclass(float, int) 为 False，因为 float 不是 int 的子类。
#
#.1 多重继承
#
# class DerivedClass(Base1, Base2, Base3):
#   ...
# 在大多数情况下，在最简单的情况下，你能想到的搜索属性从父类继承的深度优先，左到右，而不是搜索两次在同一个类层次结构中，其中有一个重叠。
# 因此，如果在 DerivedClassName （示例中的派生类）中没有找到某个属性，就会搜索 Base1，然后（递归的）搜索其基类，如果最终没有找到，就搜索 Base2，以此类推。
#
# 实际上，super() 可以动态的改变解析顺序。这个方式可见于其它的一些多继承语言，类似 call-next-method，比单继承语言中的 super 更强大 。
#
# 动态调整顺序十分必要的，因为所有的多继承会有一到多个菱形关系（指有至少一个祖先类可以从子类经由多个继承路径到达）。
# 例如，所有的 new-style 类继承自 object ，所以任意的多继承总是会有多于一条继承路径到达 object 。
#
# 为了防止重复访问基类，通过动态的线性化算法，每个类都按从左到右的顺序特别指定了顺序，每个祖先类只调用一次，这是单调的（意味着一个类被继承时不会影响它祖先的次序）。
# 总算可以通过这种方式使得设计一个可靠并且可扩展的多继承类成为可能。进一步的内容请参见 http://www.python.org/download/releases/2.3/mro/ 。
# 

#6. 私有变量
#
# 只能从对像内部访问的“私有”实例变量，在 Python 中不存在。然而，也有一个变通的访问用于大多数 Python 代码：
#   以一个下划线开头的命名（例如 _spam ）会被处理为 API 的非公开部分（无论它是一个函数、方法或数据成员）。它会被视为一个实现细节，无需公开。
#
# 因为有一个正当的类私有成员用途（即避免子类里定义的命名与之冲突），Python 提供了对这种结构的有限支持，称为 name mangling （命名编码） 。
# 任何形如 __spam 的标识（前面至少两个下划线，后面至多一个），被替代为 _classname__spam ，去掉前导下划线的 classname 即当前的类名。此语法不关注标识的位置，只要求在类定义内。
#
# 名称重整是有助于子类重写方法，而不会打破组内的方法调用。例如:
class Mapping:
  def __init__(self, iterable):
    self.items_list = []
    self.__update(iterable)

  def update(self, iterable):
    for item in iterable:
      self.items_list.append(item)

  __update = update

class MappingSubClass(Mapping):
  def update(self, keys, values):
    for item in zip(keys, values):
      self.items_list.append(item)
  

#7. 补充
#
# 有时类似于 Pascal 中“记录（record）”或 C 中“结构（struct）”的数据类型很有用，它将一组已命名的数据项绑定在一起。一个空的类定义可以很好的实现它:
#
class Employee:
  pass

john = Employee()

john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 100000

# 某一段 Python 代码需要一个特殊的抽象数据结构的话，通常可以传入一个类，事实上这模仿了该类的方法。
# 例如，如果你有一个用于从文件对象中格式化数据的函数，你可以定义一个带有 read() 和 readline() 方法的类，以此从字符串缓冲读取数据，然后将该类的对象作为参数传入前述的函数。
#
# 实例方法对象也有属性：m.__self__ 是一个实例方法所属的对象，而 m.__func__ 是这个方法对应的函数对象。
#

#8. 异常也是类

# 发生的异常其类型如果是 except 子句中列出的类，或者是其派生类，那么它们就是相符的（反过来说－－发生的异常其类型如果是异常子句中列出的类的基类，它们就不相符）。
# 例如，以下代码会按顺序打印 B，C，D:
# 简单的说就是基类可以捕获派生类异常，而派生类不能捕获基类异常。
#
class B(Exception):
  pass
class C(B):
  pass
class D(C):
  pass

for cls in [B, C, D]:
  try:
    raise cls()
  except D:
    print("D")
  except C:
    print("C")
  except B:
    print("B")

for cls in [B, C, D]:
  try:
    raise cls()
  except B:
    print("B")
  except C:
    print("C")
  except D:
    print("D")

# 上面的只会被基类捕获。

