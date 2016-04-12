# 基于生成器的实现

我们还可以用装饰器(decorators)和生成器(generators)来实现上下文管理器。  
Python有个```contextlib```模块专门用于这个目的。我们可以使用一个生成器函数来实现一个上下文管理器，而不是使用一个类。  
让我们看看一个基本的，没用的例子：

```python
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()
```

OK啦！这个实现方式看起来更加直观和简单。然而，这个方法需要关于生成器、```yield```和装饰器的一些知识。在这个例子中我们还没有捕捉可能产生的任何异常。它的工作方式和之前的方法大致相同。

让我们小小地剖析下这个方法。
1. Python解释器遇到了```yield```关键字。因为这个缘故它创建了一个生成器而不是一个普通的函数。
2. 因为这个装饰器，```contextmanager```会被调用并传入函数名（```open_file```）作为参数。
3. ```contextmanager```函数返回一个以```GeneratorContextManager```对象封装过的生成器。
4. 这个```GeneratorContextManager```被赋值给```open_file```函数，我们实际上是在调用```GeneratorContextManager```对象。

那现在我们既然知道了所有这些，我们可以用这个新生成的上下文管理器了，像这样：
```python
with open_file('some_file') as f:
    f.write('hola!')
```
