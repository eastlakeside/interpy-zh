---
parent: 数据结构
nav_order: 3
---


# 类

类是 Python 的核心。它们给了我们很大的力量，但很容易滥用这种力量。在本节中，我将分享一些与 Python 中的类相关的模糊技巧和警告。我们开始吧！

## 实例和类变量

大多数初学者甚至一些高级 Python 程序员都不理解实例和类变量之间的区别。他们缺乏理解迫使他们错误地使用这些不同类型的变量。让我们理解他们。

基本区别是：

- 实例变量用于每个对象都是唯一的数据。
- 类变量用于在类的不同实例之间共享的数据。

我们来看一个例子：

```python
class Cal(object):
    # pi 是类变量
    pi = 3.142

    def __init__(self, radius):
        # self.radius 是实例变量
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

a = Cal(32)
a.area()
# Output: 3217.408
a.pi
# Output: 3.142
a.pi = 43
a.pi
# Output: 43

b = Cal(44)
b.area()
# Output: 6082.912
b.pi
# Output: 3.142
b.pi = 50
b.pi
# Output: 50
```

使用不可变类变量时没有太多问题。因为一切正常，初学者不会尝试更多地了解这个主题，这是主要原因！
如果你还认为如果使用不正确，实例和类变量不会导致任何问题，看看下一个示例。

```python
class SuperClass(object):
    superpowers = []

    def __init__(self, name):
        self.name = name

    def add_superpower(self, power):
        self.superpowers.append(power)

foo = SuperClass('foo')
bar = SuperClass('bar')
foo.name
# Output: 'foo'

bar.name
# Output: 'bar'

foo.add_superpower('fly')
bar.superpowers
# Output: ['fly']

foo.superpowers
# Output: ['fly']
```

这是可变类变量错误使用的美妙之处。为了使你的代码安全抵御这种意外攻击，请确保你不使用可变类变量。
只有当你知道自己在做什么时，才可以使用它们。

## 新样式的类

Python 2.1 中引入了新的样式类，但是现在很多人都不知道它们！之所以如此，是因为 Python 还支持
旧样式类以保持向后兼容性。我已经说了很多关于新旧的事情，但我没有告诉你这个差异。那么主要区别在于：

- 旧的基类不会从任何东西继承。
- 新样式基类继承自 ```object```。

一个非常基本的例子是：

```python
class OldClass():
    def __init__(self):
        print('I am an old class')

class NewClass(object):
    def __init__(self):
        print('I am a jazzy new class')

old = OldClass()
# Output: I am an old class

new = NewClass()
# Output: I am a jazzy new class
```

从 ```object``` 继承允许新样式类利用一些 __魔法__。 一个主要优点是您可以使用一些有用的优化，如 ```__slots__```。 您可以使用 ```super()``` 和描述符等。 底线？总是尝试使用新式的类。

**注意**：Python 3 只有新式的类。无论您是否从 ```object``` 继承，都无关紧要。但是，建议您仍然从 ```object``` 继承。

## 魔术方法

Python 的类以其神奇的方法而闻名，通常称为 **dunder**（双下划线）方法。我将讨论其中的一些。

- ```__init__```

它是一个类初始化器。 每当创建一个类的实例时，都会调用其 ```__init__``` 方法。 例如：

```python
class GetTest(object):
    def __init__(self):
        print('Greetings!!')
    def another_method(self):
        print('I am another method which is not'
              ' automatically called')

a = GetTest()
# Output: Greetings!!

a.another_method()
# Output: I am another method which is not automatically
# called
```

你可以看到在实例在创建后会立即调用 ```__init__```。 你还可以在初始化期间将参数传递给类。像这样：

```python
class GetTest(object):
    def __init__(self, name):
        print('Greetings!! {0}'.format(name))
    def another_method(self):
        print('I am another method which is not'
              ' automatically called')

a = GetTest('yasoob')
# Output: Greetings!! yasoob

# Try creating an instance without the name arguments
b = GetTest()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: __init__() takes exactly 2 arguments (1 given)
```

我相信你现在了解了 ```__init__``` 方法。

- ```__getitem__```

在类中实现 **getitem** 允许其实例使用 ```[]```（索引器）运算符。这是一个例子：

```python
class GetTest(object):
    def __init__(self):
        self.info = {
            'name':'Yasoob',
            'country':'Pakistan',
            'number':12345812
        }

    def __getitem__(self,i):
        return self.info[i]

foo = GetTest()

foo['name']
# Output: 'Yasoob'

foo['number']
# Output: 12345812
```

如果没有 ```__getitem__```方法，我们会遇到以下错误：

```python
>>> foo['name']

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'GetTest' object has no attribute '__getitem__'
```
