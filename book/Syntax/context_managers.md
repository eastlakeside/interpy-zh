---
parent: 语法
nav_order: 7
---

# 上下文管理器

上下文管理器（Context managers）允许你在有需要的时候，精确地分配和释放资源。  

使用上下文管理器最广泛的案例就是 ```with``` 语句了。
想象下你有两个需要结对执行的相关操作，然后还要在它们中间放置一段代码。
上下文管理器就是专门让你做这种事情的。举个例子：

```python
with open('some_file', 'w') as opened_file:
    opened_file.write('Hola!')
```

上面这段代码打开了一个文件，往里面写入了一些数据，然后关闭该文件。如果在往文件写数据时发生异常，它也会尝试去关闭文件。上面那段代码与这一段是等价的：

```python
file = open('some_file', 'w')
try:
    file.write('Hola!')
finally:
    file.close()
```

当与第一个例子对比时，我们可以看到，通过使用 ```with```，许多样板代码（boilerplate code）被消掉了。 这就是 ```with``` 语句的主要优势，它确保我们的文件会被关闭，而不用关注嵌套代码如何退出。

上下文管理器的一个常见用例，是资源的加锁和解锁，以及关闭已打开的文件（就像我已经展示给你看的）。

让我们看看如何来实现我们自己的上下文管理器。这会让我们更完全地理解在这些场景背后都发生着什么。


# 基于类的实现

一个上下文管理器的类，最起码要定义 ```__enter__``` 和 ```__exit__``` 方法。
让我们来构造我们自己的开启文件的上下文管理器，并学习下基础知识。

```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
```

通过定义 ```__enter__``` 和 ```__exit__``` 方法，我们可以在```with```语句里使用它。我们来试试：

```python
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
```

我们的 ```__exit__``` 函数接受三个参数。这些参数对于每个上下文管理器类中的 ```__exit__``` 方法都是必须的。我们来谈谈在底层都发生了什么。

1. ```with``` 语句先暂存了 ```File``` 类的 ```__exit__``` 方法。
2. 然后它调用 ```File``` 类的 ```__enter__``` 方法。
3. ```__enter__``` 方法打开文件并返回给 ```with``` 语句。
4. 打开的文件句柄被传递给 ```opened_file``` 参数。
5. 我们使用 ```.write()``` 来写文件。
6. ```with``` 语句调用之前暂存的 ```__exit__``` 方法。
7. ```__exit__``` 方法关闭了文件。


# 处理异常

我们还没有谈到 ```__exit__``` 方法的这三个参数：```type```，```value``` 和 ```traceback```。
在第4步和第6步之间，如果发生异常，Python 会将异常的 ```type```，```value``` 和 ```traceback``` 传递给 ```__exit__``` 方法。
它让 ```__exit__``` 方法来决定如何关闭文件以及是否需要其他步骤。在我们的案例中，我们并没有注意它们。

那如果我们的文件对象抛出一个异常呢？万一我们尝试访问文件对象的一个不支持的方法。举个例子：

```python
with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function('Hola!')
```

我们来列一下，当异常发生时，```with``` 语句会采取哪些步骤。

1. 它把异常的 ```type```，```value``` 和 ```traceback``` 传递给 ```__exit__```方法。
2. 它让 ```__exit__``` 方法来处理异常。
3. 如果 ```__exit__``` 返回的是 True，那么这个异常就被优雅地处理了。
4. 如果 ```__exit__``` 返回的是 True 以外的任何东西，那么这个异常将被 ```with``` 语句抛出。

在我们的案例中，```__exit__``` 方法返回的是 ```None``` （如果没有 ```return``` 语句那么方法会返回 ```None```）。因此，```with``` 语句抛出了那个异常。

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'file' object has no attribute 'undefined_function'
```

我们尝试下在 ```__exit__``` 方法中处理异常：

```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Output: Exception has been handled
```

我们的 ```__exit__``` 方法返回了 ```True```，因此没有异常会被 ```with``` 语句抛出。

这还不是实现上下文管理器的唯一方式。还有一种方式，我们会在下一节中一起看看。

# 基于生成器的实现

我们还可以用装饰器（decorators）和生成器（generators）来实现上下文管理器。
Python 有个 ```contextlib``` 模块专门用于这个目的。我们可以使用一个生成器函数来实现一个上下文管理器，而不是使用一个类。
让我们看看一个基本的，没用的例子：

```python
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()
```

OK啦！这个实现方式看起来更加直观和简单。然而，这个方法需要关于生成器、```yield``` 和装饰器的一些知识。在这个例子中我们还没有捕捉可能产生的任何异常。它的工作方式和之前的方法大致相同。

让我们小小地剖析下这个方法。

1. Python 解释器遇到了 ```yield``` 关键字。因为这个缘故它创建了一个生成器而不是一个普通的函数。
2. 因为这个装饰器，```contextmanager``` 会被调用并传入函数名（```open_file```）作为参数。
3. ```contextmanager``` 函数返回一个以 ```GeneratorContextManager``` 对象封装过的生成器。
4. 这个 ```GeneratorContextManager``` 被赋值给 ```open_file``` 函数，我们实际上是在调用 ```GeneratorContextManager``` 对象。

那现在我们既然知道了所有这些，我们可以用这个新生成的上下文管理器了，像这样：

```python
with open_file('some_file') as f:
    f.write('hola!')
```
