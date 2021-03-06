#!/usr/bin/env python
# _*_ coding:utf8 _*_
# Kevien：vianus@qq.com  CreatDate:2016-12-22


'''
Python内建函数：

Python提供了许多内建函数。下面按函数名字母顺序一一列出并作介绍。

abs(x)
返回一个数的绝对值。参数可以是一个普通整数、长整数或浮点数。如果参数是复数， 则它的值被返回。如：若a=x+yi, 则abs(a)=sqrt(x^2+y^2)。

all(iterable) 
如果可编历对象中的所有元素都是真值，则返回True。相当于：
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True
该函数是2.5版本中新增的。

any(iterable) 
只要可编历对象中有一个元素为真值，就返回True。等价于：
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
该函数是2.5版本中新增的。

basestring() 
（注：basestring是一个可调用对象。）basestring是str与unicode的父类，它是一个抽象类，不能直接被调用或实例化，但可以用它来测试一个对象是否是str或unicode的实例: isinstance(obj, basestring)，等效于isinstance(obj, (str, unicode))。
该函数是2.3版本中新增的。

bin(x) 
将一个整数转换成二进制字符串。结果是一个合法的Python表达式。如果参数x不是一个整数对象（int object），它必须定义__index__()方法，并返回一个整数。
该函数是2.6版本中新增的。

bool([x])
使用标准真值测试过程(standard truth testing procedure)将一个值转换成布尔型。如果参数x省略或为假值（如：0, 空字符串，None），返回False；否则总是返回True。bool也是类型，它是int类型的子类。但不能从bool类型派生子类。它只有两个实例：True和False。
该函数是2.21版本中新增的。
在2.3版本中有所改变：如果没有参数传入，函数返回False。

callable(object) 
如果参数object是可调用的，返回True，否则返回False。即使函数返回True，调用该对象仍然有可能会失败；但是如果返回False，则调用对象肯定失败。注意：类都是可调用的（通过调用类返回一个新实例）。定义了__call__()方法的实例都是可调用的。

chr(i) 
将assii码为i的整数转换成只包含一个字符的字符串。例如：chr(97)返回字符串’a’。参数i必须在0—255范围内，否则会触发ValueError异常。与之对应的一个函数是ord(c)，它将字符转换成整数。也可以参考一下unichr()。

classmethod(function) 
该函数返回一个类方法。类方法显式的接收第一个参数作为类类型，就如实例方法接收第一个参数作为对当前实例的引用。可以使用下面的语法定义一个类方法：
class C:
    @classmethod
def f(cls, arg1, arg2, ...): ...
@classmethod是一个函数修饰符----可以在Function definitions中查询更多关于函数定义描述的信息。
可以通过类（如：C.f()）或实例（如：C().f()）调用类方法。如果在派生类中调用父类的类方法，派生类对象（derived class object） 将作为第一个参数被传入类方法。
Python类方法与C++或Java中的静态方法有区别。可以查询本章中对staticmethod的介绍来了解这些知识。
更多关于类方法的信息，可以参考：The standard type hierarchy.
该函数是2.2版本中新增的。在2.4版本中作了修改：添加了对函数装饰语法的支持。

cmp(x, y) 
比较两个对象并根据比较结果返回一个整数。如果x < y， 返回一个负数，如果 x > y返回一个正数，如果x == y返回0。

compile(source, filename, mode[, flags[, dont_inherit]])
将源代码编译成代码对象(code object)或AST对象。可以通过exec语句来执行代码对象，或通过eval()来求值。参数source可以是字符串或AST对象。更多关于AST对象的信息，可以参考ast模块文档。
参数mode指定了代码编译的模式。它可以是：
    “exec”：代码段
“eval”: 单个表达式
“single”: 单条交互式语句
可选参数 flags和dot_inherit控制 影响代码编译的将来语句。两个参数的默认值都是0，

complex([real[, imag]]) 
创建一个值为 real + imag * j 的复数，或将一个字符串或数字转换为一个复数。如果第一个参数是字符串，它将被作为复数解析，同时不能提供第二个参数。第二个参数不能是字符串。每个参数可以是任何的数字类型（包括复数类型）。参数imag的默认值为0。如果两个参数都省略，返回0j。

delattr(object, name) 
参数是一个对象和字符串。字符串必须是对象属性的名称。函数删除对象的属性。如：delattr(x, “foobar”)，相当于语句：del x.foobar。与delattr对应的函数是setattr，用于设置对象的属性。

dict([arg]) 
创建一个字典对象。可选的参数arg用于初始化字典项。字典类型在Mapping Types — dict章中进行介绍。关于其他的容器，可以参考list, set,tuple，collections模块。

dir([object]) 
如果省略参数，函数返回局部区域内的变量列表。如果参数没有省略，函数尝试将该参数对象的所有合法属性名称保存到列表中并返回该列表。
如果对象定义了__dir__()方法，那么该方法将被调用，并返回属性列表。允许对象通过实现__getattr__()和__getattribute__()方法来自定义dir()返回对象的属性。
如果对象没有定义__dir__()，dir()尝试从对象的__dict__属性（如果定义了__dict__）和对象所属类型中获取信息。dir()返回的结果不必是完整的，如果对象定义了__getattr__()方法，那么结果可能不准确。
默认的dir()实现针对不同类型的对象可能有不同的行为，它尝试去获取更多相关的信息，而不是全部的信息：
如果对象是模块对象(module object)，结果列表包含所有模块中定义的属性的名称。
如果对象是类型或类对象，结果列表包含该类型所有的属性名称，包括从父类继承的。否则，结果列表包含对象的所有属性名称、对象所属类型的属性名称，以及父类的所有属性名称。结果列表根据属性的名称字母顺序保存。
>>> import struct
>>> dir()   # doctest: +SKIP
['__builtins__', '__doc__', '__name__', 'struct']
>>> dir(struct)   # doctest: +NORMALIZE_WHITESPACE
['Struct', '__builtins__', '__doc__', '__file__', '__name__',
 '__package__', '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
 'unpack', 'unpack_from']
>>> class Foo(object):
...     def __dir__(self):
...         return ["kan", "ga", "roo"]
...
>>> f = Foo()
>>> dir(f)
['ga', 'kan', 'roo']

divmod(a, b) 
接收两个数字（复数除外）作为参数，返回一对值：商，余数。对于不同类型的操作数，按二进制算术运算法则进行计算。对于普通整数与长整数，结果为：(a / b, a % b)。对于浮点数，结果为：(q, a % b)，其中q = math.floor(a / b)，如果q < 1，q = 1。无论如何，q * b + a % b总是非常接近于a，如果a不能整除b，那么：0 <= abs(a % b) < abs(b)。
在2.3版本中作了修改：不赞成使用复数作为参数。

enumerate(sequence[, start=0]) 
返回一个enumerate对象。参数sequence必须是一个序列类型，iterator,或者其他支持编历的对象。通过调用enumerate()返回的iterator，它的next()方法返回一个包含 计数（由参数start开始，默认值为0）和对应值 的元组。可以使用Enumerate()来获取一个带索引的序列：(0, seq[0]), (1, seq[1]), (2, seq[2]),...
例如：
>>> for i, season in enumerate(['Spring', 'Summer', 'Fall', 'Winter']):
...     print i, season
0 Spring
1 Summer
2 Fall
3 Winter
该函数是2.3版本中新增的。
在2.6版本中，增加了start 参数。

eval(expression[, globals[, locals]]) 
参数expression是一个字符串，可选的globals参数必须是一个字典，可选的locals必须是一个映射对象（mapping object）。
Expression参数作为一个Python表达式而被解析并求值(evaluate)，它使用globals与locals字典作为全局和本地变量。globals参数的默认值为当前的全局变量。locals参数默认为globals。 如果两个参数都省略，那么eval()会在 当前上下文 中执行。执行过程中的异常都会被认为是语法错误异常。下面是使用eval的例子:
X = 1
Print eval(‘x + 1’)
expression参数也可以是一个代码对象（通过compile()创建），如果代码对象使用’exec’模式进行编译（如：eval(compile(‘3 + 4’, ‘<string>’, “exec”)），eval()函数将返回None。
提示：exec（）支持动态语句执行，使用execfile()来执行文件中的语句。Globals(), locals()分别返回全局变量和局部变量的字典，它们可以在调用eval, execfile时作为参数传入。

execfile(filename[, globals[, locals]]) 
这个函数与exec语句很像，但是它接收一个文件路径作为参数，并执行文件中的内容。它与import语句不同：它没有使用模块管理—它只是无条件的读取文件内容并执行，而没有创建一个新的模块。
Execfile()的globals参数与locals参数的含义和eval()一样，但函数的返回值为None。

file(filename[, mode[, bufsize]]) 
file类型的构造函数，它的参数与open()方法的参数的含义一致。open()方法将在下面介绍。
当要打开一个文件时，通常使用open()来代替file()。file()更适合在类型测试的时候来使用（如：isinstance(f, fle)）。该函数是在此2.2版本中新增的。

filter(function, iterable) 
分别对可编历对象中的元素应用函数，将结果为True的元素组成新的列表并返回（不改变原有列表。）。 iterable参数可以是一个序列、一个支持编历的容器对象、也可以是一个iterator对象。如果参数是字符串类型或者tuple类型，那么返回的结果也是原来的类型；否则它总是返回一个列表(list)类型。如果function为None，则恒等函数（identity function）被作为筛选函数（过滤掉非真值元素）
函数等效为：
function不为None: [item for item in iterable if function(item)]
Function为None: [item for item in iterable if item]

float([x]) 
将一个字符串或数字转换为浮点数。如果参数是字符串，它可能包含符号或小数点，字符串参数也可以是”+nan”,”-nan” 或”+inf”,”-info”；否则，参数必须是普通整数或长整数，或一个浮点数。浮点数将直接被返回。如果没有提供参数，函数返回0.0。
注意：
如果参数是字符串，函数可能会返回NaN( Not a Number)，Infinity（无穷大），这依赖于低层的C语言库。Float可能接收”nan”来表示一个非数字，inf和-inf来表示一个正无穷和负无穷。对于nan，”+”, “-“符号将被忽略。Float通过使用”nan”, “inf”, “-inf”来表示NaN, 正无穷，负无穷。

format(value[, format_spec]) 
     按指定格式表示一个值。对格式的解析依赖于值参数。有一套标准的格式语法用于大部分Python内置类型。
注意：
Format(value, format_spec)仅仅调用value.__format__(format_spec)。该函数是2.6版本中新增的。

frozenset([iterable]) 
Return a frozenset object, optionally with elements taken from iterable. The frozenset type is described in Set Types — set, frozenset.
For other containers see the built in dict, list, and tuple classes, and the collections module.
New in version 2.4.

getattr(object, name[, default]) 
获取对象指定属性的值。参数name必须是一个字符串，如果name为对象中某个属性的名字，该属性的值将被返回。例如：getattr(x,“foobar”)等效于x.foobar。如果属性名字不存在，参数default将被返回。如果函数名不存在且没有提供default参数，将触发AttributeError异常。

globals() 
返回当前模块的全局变量字典。(如果在方法或函数中调用globals()，返回的是定义该方法或函数的模块的全局变量字典，而不是调用该函数或方法的所在的模块（的全局变量字典))
hasattr(object, name) 
判断对象是否存在指定名字的属性。（hasattr通过调用getattr(object, name)，根据是否抛出异常来判断属性名是否存在）

hash(object) 
返回对象的哈希值。哈希值是整数。它被应用于字典的键，在查找的时候进行快速比较。数值对象的哈希值与值相同（即使他们有不同的类型，如：
Hash(1.0) == 1.0 #True
hash(1.0) == hash(1) #True）

help([object]) 
调用系统帮助。（该函数可以与系统进行交互）。如果没有提供参数，交互式帮助系统帮助将在解析器控制台上启动。如果参数是一个字符串，它将作为模块、函数、类型、方法、关键字或文件主题的名称查询，并将相关帮助信息显示到控制台上；如果参数是其他类型的对象，对象的帮助信息将创建(并显示在控制台上)。该函数通过site模块被添加到内建命名域内。该函数是在2.2版本中新增的。

hex(x) 
获取一个整数的十六进制字符串表示。结果是一个合法的Python表达式。2.4版本之前只返回一个无符号字面值。

id(object) 
返回对象的标识符（identity）。标识符是一个整数（或长整数），在对象生命周期内保证唯一且不会改变。不重叠作用域内的两个对象可能会有一样的标识符。（当前实现中，标识符返回对象在内存中的地址。）

input([prompt]) 
相当于eval(raw_input(prompt))
警告：
该函数无法保证用户输入的内容是合法的，它期望一个合法的Python表达式作为输入，如果输入有语法错误，将触发SyntaxError。在求值期间出现的其他错误也会触发相应的异常。（另一方面，在写一些快速脚本作为高级应用时，这个函数非常有用。）如果已经加载了readline模块，input()函数将使用该模块提供复杂的行编辑和记载功能。应当考虑使用raw_input()函数来获取用户的一般性输入。

int([x[, radix]]) 
将一个字符串或数值转换为一个普通整数。如果参数是字符串，那么它可能包含符号和小数点。参数radix表示转换的基数（默认为10进制），它可以是[2,36]范围内的值，或者0。如果为0，系统将根据字符串的内容来解析。如果提供了参数radix，但参数x并不是一个字符串，将抛出TypeError异常；否则，参数x必须是数值（普通整数，长整数，浮点数）。通过舍去小数来转换浮点数。如果结果超出了普通整数的表示范围，一个长整数被返回。如果没有提供参数，函数返回0。
关于整数类型，可以参考：Numeric Types — int, float, long, complex.

isinstance(object, classinfo) 
如果对象是类型的实例，或该类型派生类的实例，则返回True；如果参数classinfo是类型对象(type object)同时参数object是类对象或派生类的对象，也返回True。(译者注：如：isinstance(A, type(A)))。如果参数object不是类实例或不是给定类型的实例，函数将返回False。
如果参数classinfo不是一个类，类型或 关于类、类型的元组（译者注：如：(ClassA, ClassB)），或其他相关元组，将触发TypeError异常。在2.2版本中添加了对 类型信息元组 的支持。

issubclass(class, classinfo) 
如果参数class是参数classinfo的子类，返回True。一个类被认为是它自己的子类（译者注：issubclass(ClassA, ClassA)返回True）。参数classinfo可以是多个类对象(class object)的元组，在这种情况下，元组中的每个类都会被检查。

iter(o[, sentinel]) 
返回一个iterator对象。该函数对于第一个参数的解析依赖于第二个参数。如果没有提供第二个参数，参数o必须是一个集合对象，支持编历功能（__iter__()方法）或支持序列功能(__getitem__()方法，参数为整数，从0开始)，如果不支持这两种功能，将触发TypeError异常。如果提供了第二个参数，参数o必须是一个可调用对象。在这种情况下创建一个iterator对象，每次调用iterator的next()方法来无参数的调用o，如果返回值等于参数sentinel，触发StopIteration异常，否则将返回该值。该函数是2.2版本中新增的。

len(s) 
返回对象的长度。参数可以是序列类型（字符串、元组或列表）或映射类型（如字典）。

list([iterable]) 
list的构造函数。参数iterable是可选的，它可以是序列，支持编译的容器对象，或iterator对象。该函数创建一个 元素值，顺序与 参数iterable一致的列表。如果参数iterable是一个列表，将创建该列表的一个拷贝并返回，就像语句iterable[:]。例如：list(‘abc‘)返回[‘a’, ‘b’, ‘c’]，list((1, 2, 3))返回[1, 2, 3]。如果没有提供参数，返回一个空的列表:[]。

locals() 
更新并返回一个表示当前局部变量的字典。
警告：
不要修改locals()返回的字典中的内容；改变可能不会影响解析器对局部变量的使用。
在函数体内调用locals（），返回的是自由变量(Free variables)。修改自由变量不会影响解析器对变量的使用。不能在类区域内返回自由变量。

long([x[, radix]]) 
将字符串或数字转换为长整数。如果参数是字符串，那么它可能包含符号。参数radix的意义与int()函数中的一样，只有在参数x是字符串的情况下，才给出。否则x必须是普通整数、长整数或浮点数，如果是长整数，其值将直接被返回。通过舍去小数来将浮点数转换成长整型。如果没有提供参数，函数返回0L。

map(function, iterable, ...) 
对参数iterable中的每个元素都应用function函数，并将结果作为列表返回。 如果有多个iterable参数，那么function函数必须接收多个参数，这些iterable中相同索引处的元素将并行的作为function函数的参数。如果一个iterable中元素的个数比其他少，那么将用None来扩展该iterable使元素个数一致。如果有多个iterable且function为None，map()将返回由元组组成的列表，每个元组包含所有iterable中对应索引处值。参数iterable必须是一个序列或任何可编历对象，函数返回的往往是一个列表(list)。

max(iterable[, args...][, key]) 
如果只提供iterable参数，函数返回可编历对象（如：字符串，元组或列表）中最大的非空元素。如果提供了多个参数，那么返回值最大的那个参数。可选参数key是单参数的排序函数。如果提供key参数，必须是以命名参数的形式，如：max(a, b, c, key = fun)----我不清楚参数key有什么作用？在2.5版本中修改：添加了可选的key参数。

min(iterable[, args...][, key]) 
如果只提供iterable参数，函数返回可编历对象（如：字符串，元组或列表）中最小的非空元素。如果提供了多个参数，那么返回值最小的那个参数。可选参数key是单参数的排序函数。如果提供key参数，必须是以命名参数的形式，如：max(a, b, c, key = fun)----我不清楚参数key有什么作用？

next(iterator[, default]) 
通过调用iterator的next()方法获取下一个元素。当iterator编历完的时候，如果提供default参数，该default参数将被返回，否则触发StopIteration异常。
该函数是2.6版本中新增的。

object() 
获取一个新的、无特性(featureless)对象。Object是所有类的基类。它提供的方法将在所有的类型实例中共享。该函数是2.2版本中新增的。2.3版本之后，该函数不接收任何参数。以前可以接收参数，但这些参数都被忽略。

oct(x) 
将一个整数转换为八进制字符串。结果是一个合法的Python表达式。在2.4版本之前，该函数只返回无符号的字面值。

open(filename[, mode[, bufsize]]) 
打开一个文件，返回一个file对象。如果文件无法打开，将触发IOError 异常。应该使用open()来代替直接使用file类型的构造函数打开文件。参数filename表示将要被打开的文件的路径字符串；参数mode表示打开的模式，最常用的模式有：‘r’表示读文本文件，’w’表示写文本文件，’a’表示在文件中追加文本内容。Mode的默认值是’r’。 在操作文本文件时，’/n’可能会被转换为特定平台相关的表示。
当操作的是二进制文件时，只要在模式值上添加’b’。这样提高了程序的可移植性。（有些操作系统不区别文本文件和二进制文件，这些文件都被当作文档(document)来处理，这时把模式设为二进制模式就比较合适。）
可选参数bufsize定义了文件缓冲区大小。0表示不缓冲 (unbuffered)；1表示行缓冲(line buffered)；任何其他正数表示使用该大小的缓冲区；负数表示使用系统默认缓冲区大小，对于tty设备它往往是行缓冲，而对于其他文件往往完全缓冲。如果参数被省略，使用系统默认值。

ord(c) 
将字符（长度为1的字符串）转换为整数。例如：ord(‘a’)返回整数97，ord(u’/u2020’)返回8224。

pow(x, y[, z]) 
返回x的y次方；如果提供了参数z，则返回x的y次方，并对z进行取模操作（比pow(x, y) % z效率更高）。也可以使用x**y来代替pow(x, y)

print([object, ...][, sep=' '][, end='n'][, file=sys.stdout]) 
打印对象到流文件(stream file)，通过sep参数分开，以end参数结束。参数sep, end, file必须以关键字参数的形式出现，如果提供的话。
所有非关键字参数都被转换为字符串并写入到流，通过sep分开，将end附加到末尾。参数sep和end都是字符串，也可以为None，这意味着使用默认值。如果没有对象，print()直接将end写入。
File参数必须是一个包含write(string)方法的对象。如果没有该方法或对象为None，使用默认值sys.stdout
注意：在默认情况下，print方法是不可使用的，因为它往往被认为是print语句。为了使用print()方法同时并禁用print语句，要在模块的开始处添加如下语句：
from __future__ import print_function
该函数是2.6版本中新增的。

property([fget[, fset[, fdel[, doc]]]]) 

range([start], stop[, step]) 
这是一个通过的，用于创建包含连续算术值的列表（list）。它经常被用于for循环。参数必须是普通整数。参数 step的默认值为1，参数start的默认值为0。全参数调用该函数将返回一个普通整数列表[start, start + step, start + 2 * step, ...]。如果参数step为正数，列表中的最后一个元素将是最大值，为start + i * step，小于stop；如果step为负数，列表中最后一个元素将是最小值，为start – I * step，大于stop。参数step不能为0（否则将触发ValueError异常）。
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5)
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3)
[0, 3, 6, 9]
>>> range(0, -10, -1)
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]

raw_input([prompt]) 
如果提供了prompt参数，它将被写入到标准输出（结尾没有换行符），函数然后从输入中读一行数据，转换成字符串（去除结尾的换行符）并返回。当读取EOF时，将触发EOFError异常。下面是一个例子：
>>> s = raw_input('--> ')
--> Monty Python's Flying Circus
>>> s
"Monty Python's Flying Circus"
reduce(function, iterable[, initializer]) 

reload(module) 
重新加载先前导入(imported)的模块。参数是模块对象，所以该模块必须在之前成功的导入。Reload在这种情况下非常有用：程序在运行过程中模块源代码发生改变，让Python解析器擅自加载最新版本代码。函数的返回值是模块对象。
当reload(module)执行时：Python模块的代码被重新编译，模块级(module-level)的代码被重新执行，定义新的对象信绑定到模块字典，而扩展模块的初始化函数将不会被再次调用。
就如Python中其他对象一样，原有模块的一些对象只有在其引用计算为0的时候才会被回收。
模块内的名称被更新，用于表明任何新的或改变的对象。对原有对象的引用不会重新绑定引用到新的对象。

repr(object) 
返回一个对象的字符串表示。有时可以使用这个函数来访问操作。对于许多类型来说，repr()尝试返回一个字符串，eval()方法可以使用该字符串产生对象；否则用尖括号括起来的，包含类名称和其他额外信息（如：对象名字，在内存中的地址）的字符串被返回。类可以通过定义__repr__()方法来控制它的对象的输出。

reversed(seq) 
返回一个逆序的iterator对象。参数seq必须是一个包含__reversed__()方法的对象或支持序列操作（__len__()和__getitem__()）
该函数是2.4版本中新增的。

round(x[, n])
对参数x的第n+1位小数进行四舍五入，返回一个小数位数为n的浮点数。参数n的默认值是0。结果是一个浮点数。如：round(0.5) 结果 为 1.0

set([iterable]) 

setattr(object, name, value) 
该方法与getattr()相对应。参数分别是一个对象、字符串和值。字符串可能是一个存在的属性名或一个新的属性名，该函数将值赋给对象的属性。如：setattr(x, ‘fllbar’, 123)等价于x.foobar = 123。

slice([start], stop[, step]) 

sorted(iterable[, cmp[, key[, reverse]]]) 

staticmethod(function) 
返回一个静态方法。静态方法不显式的接收第一个参数（作为类型）。使用下面的语法声明一个静态方法：
lass C:
    @staticmethod
    def f(arg1, arg2, ...): ...
可以在类中调用静态方法（如：C.f()），，也可以在对象上调用（如：C().f()）。
Python中的静态方法与java或C++中的静态方法类似，更详细的信息，可以参考：classmethod()
该函数是2.2版本中新增的。

str([object]) 
获取对象的字符串表示。对于字符串参数，函数直接返回。Repr()与str()之间的不同在于：str()返回的字符串可能不被eval()所接收求值，而仅仅返回一个可打印的字符串。如果没有提供参数，空字符串将被返回。

sum(iterable[, start]) 
先计算可编历对象中的元素之和，再与start相加。参数start的默认值为0。可编历对象的元素通过是数字，不能为字符串。通过调用’’.join(sequence)可以快速正确的连接一个字符串序列。注意：sum(range(n), m)等价于：reduce(operator.add, range(n), m)。对高精度的浮点数进行求和时，可以使用math.fsum().
super(type[, object-or-type]) 
返回一个可以通过委托方法调用父类型或兄弟类型的代理对象。在重写方法中使用它来访问父类中的虚方法，

tuple([iterable]) 
返回一个元组，它的元素值及元素的顺序与iterable中的一致。参数iterable可以是一个序列，或者iterator对象。如果iterable本身也是一个元组，它将被原封不支的返回。例如：tuple(‘abc’)将返回(‘a’, ‘b’, ‘c’)，tuple([1, 2, 3])将返回(1, 2, 3)。如果没有提供参数，函数返回一个空元组。

type(object) 
返回对象的类型。返回值是类型对象(type object)，建议使用isinstance()来检测对象的类型。含有三个参数的type()函数是type类的构造函数，在下面详细介绍。

type(name, bases, dict) 
返回一个类对象。它本质上是一个动态形式的类定义语句（可以动态的创建新类型）。参数name作为__name__的值，为新类型的名称，参数bases是一个元组，表示新类型的父类，作为__bases__的值；参数dict是一个字典，表示类范围成员的定义，作为__dict__的值。例如：下面两段语句创建同一类型对象：
>>> class X(object):
...     a = 1
>>> X = type('X', (object,), dict(a=1))

unichr(i) 
返回整数的unicode字符串。如：unichar(97)返回字符串 u’a’。
unicode([object[, encoding[, errors]]]) 

vars([object]) 
如果没有提供参数，返回一个表示当前局部变量表的字典。如果输入一个模块对象、类对象或类实例对象（或其他任何含有__dict__属性的东西），返回一个表示该对象变量表的字典。

xrange([start], stop[, step]) 
这个函数与range()非常像，但它返回一个xrange对象而不是列表。这是一个不透明的序列对象，可以产生像对应列表一样的值但不同时保存它们（在内存里）。Xrange相比于range的优点在于：使用xrange占用的内存更少。

zip([iterable, ...]) 
函数返回一个元组列表，其中第n个元组的元素由所有参数序列的第n个元素组成。返回列表的长度等于参数中长度最短的序列的长度。如果多个参数序列的长度一致，那么zip() 如果只有一个参数，那么返回的序列中，元素的长度为1。如果没有提供参数，返回一个空列表。
>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
>>> x2, y2 = zip(*zipped)
>>> x == x2, y == y2
True
该函数是2.0版本中新增的。在2.4版本之前，调用zip()时至少要提供一个参数，否则将触发TypeError异常。
__import__(name[, globals[, locals[, fromlist[, level]]]]) 
这是一个高级函数，在平常编程中很少用到。使用import语句加载模块时会调用该函数。很少直接使用__import__()函数，除非模块的名称在运行时得到。

'''


