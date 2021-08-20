---
parent: 语法
nav_order: 6
---

# ```*args``` 和 ```**kwargs```

我观察到，大部分新的 Python 程序员都需要花上大量时间理解清楚 ```*args``` 和 ```**kwargs``` 这两个魔法变量。那么它们到底是什么?

首先让我告诉你，其实并不是必须写成 ```*args``` 和 ```**kwargs```。只有变量前面的 ```*```（星号）才是必须的。你也可以写成 ```*var``` 和 ```**vars```。而写成 ```*args``` 和 ```**kwargs``` 只是一个通俗的命名约定。那就让我们先看一下 ```*args``` 吧。

# ```*args``` 的用法

```*args``` 和 ```**kwargs``` 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。

这里的不定的意思是：预先并不知道，函数使用者会传递多少个参数给你，所以在这个场景下使用这两个关键字。```*args``` 是用来发送一个非键值对的可变数量的参数列表给一个函数。

这里有个例子帮你理解这个概念：

```python
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
```

这会产生如下输出：

```python
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
```

我希望这解决了你所有的困惑。那接下来让我们谈谈 ```**kwargs```。


# ```**kwargs``` 的用法

```**kwargs``` 允许你将不定长度的**键值对**，作为参数传递给一个函数。如果你想要在一个函数里处理**带名字的参数**，你应该使用```**kwargs```。

这里有个让你上手的例子:

```python
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))


>>> greet_me(name="yasoob")
name == yasoob
```

现在你可以看出我们怎样在一个函数里，处理了一个**键值对**参数了。

这就是 ```**kwargs``` 的基础，而且你可以看出它有多么管用。接下来让我们谈谈，你怎样使用 ```*args``` 和 ```**kwargs``` 来调用一个参数为列表或者字典的函数。


# 使用 ```*args``` 和 ```**kwargs``` 来调用函数

那现在我们将看到怎样使用 ```*args``` 和 ```**kwargs``` 来调用一个函数。假设，你有这样一个小函数：

```python
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
```

你可以使用```*args```或```**kwargs```来给这个小函数传递参数。下面是怎样做：

```python
# 首先使用 *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# 现在使用 **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```

### 标准参数与 ```*args```、```**kwargs``` 在使用时的顺序

那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：

```python
some_func(fargs, *args, **kwargs)
```


# 什么时候使用它们？

这还真的要看你的需求而定。

最常见的用例是在写函数装饰器的时候（会在另一章里讨论）。

此外它也可以用来做猴子补丁（monkey patching）。猴子补丁的意思是在程序运行时（runtime）修改某些代码。打个比方，你有一个类，里面有个叫 ```get_info``` 的函数会调用一个API并返回相应的数据。如果我们想测试它，可以把API调用替换成一些测试数据。例如：

```python
import someclass

def get_info(self, *args):
    return "Test data"

someclass.get_info = get_info
```

我敢肯定你也可以想象到一些其他的用例。
