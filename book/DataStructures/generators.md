---
parent: 数据结构
nav_order: 1
---


# 生成器（Generators）

首先我们要理解迭代器(iterators)。根据维基百科，迭代器是一个让程序员可以遍历一个容器（特别是列表）的对象。然而，一个迭代器在遍历并读取一个容器的数据元素时，并不会执行一个迭代。你可能有点晕了，那我们来个慢动作。换句话说这里有三个部分：

- 可迭代对象（Iterable）
- 迭代器（Iterator）
- 迭代（Iteration）

上面这些部分互相联系。我们会先各个击破来讨论他们，然后再讨论生成器（generators）。

# 可迭代对象（Iterable）

Python中任意的对象，只要它定义了可以返回一个迭代器的 ```__iter__``` 方法，或者定义了可以支持下标索引的 ```__getitem__``` 方法（这些双下划线方法会在其他章节中全面解释），那么它就是一个可迭代对象。简单说，可迭代对象就是能提供迭代器的任意对象。那迭代器又是什么呢？

# 迭代器（Iterator）

任意对象，只要定义了 ```next```（Python2） 或者 ```__next__``` 方法，它就是一个迭代器。就这么简单。现在我们来理解迭代（iteration）。

# 迭代（Iteration）

用简单的话讲，它就是从某个地方（比如一个列表）取出一个元素的过程。当我们使用一个循环来遍历某个东西时，这个过程本身就叫迭代。现在既然我们有了这些术语的基本理解，那我们开始理解生成器吧。

# 生成器(Generators)

生成器也是一种迭代器，但是你只能对其迭代一次。这是因为它们并没有把所有的值存在内存中，而是在运行时生成值。你通过遍历来使用它们，要么用一个 “for” 循环，要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是 ```yield``` (暂且译作“生出”)一个值。这里有个生成器函数的简单例子：

```python
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)

# Output: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

这个案例并不是非常实用。生成器最佳应用场景是：你不想同一时间将所有计算出来的大量结果集分配到内存当中，特别是结果集里还包含循环。

> 译者注：这样做会消耗大量资源

许多 Python 2 里的标准库函数都会返回列表，而 Python 3 都修改成了返回生成器，因为生成器占用更少的资源。  

下面是一个计算斐波那契数列的生成器：

```python
# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
```

函数使用方法如下：

```python
for x in fibon(1000000):
    print(x)
```

用这种方式，我们可以不用担心它会使用大量资源。然而，之前如果我们这样来实现的话：

```python
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
```

这也许会在计算很大的输入参数时，用尽所有的资源。我们已经讨论过生成器使用一次迭代，但我们并没有测试过。在测试前你需要再知道一个Python内置函数：```next()```。它允许我们获取一个序列的下一个元素。那我们来验证下我们的理解：

```python
def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
print(next(gen))
# Output: Traceback (most recent call last):
#            File "<stdin>", line 1, in <module>
#         StopIteration
```

我们可以看到，在 ```yield``` 掉所有的值后，```next()``` 触发了一个 ```StopIteration``` 的异常。基本上这个异常告诉我们，所有的值都已经被 ```yield``` 完了。你也许会奇怪，为什么我们在使用 ```for``` 循环时没有这个异常呢？啊哈，答案很简单。```for``` 循环会自动捕捉到这个异常并停止调用 ```next()```。你知不知道Python中一些内置数据类型也支持迭代哦？我们这就去看看：

```python
my_string = "Yasoob"
next(my_string)
# Output: Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: str object is not an iterator
```

好吧，这不是我们预期的。这个异常说那个 ```str``` 对象不是一个迭代器。对，就是这样！它是一个可迭代对象，而不是一个迭代器。这意味着它支持迭代，但我们不能直接对其进行迭代操作。那我们怎样才能对它实施迭代呢？是时候学习下另一个内置函数，```iter```。它将根据一个可迭代对象返回一个迭代器对象。这里是我们如何使用它：

```python
my_string = "Yasoob"
my_iter = iter(my_string)
next(my_iter)
# Output: 'Y'
```

现在好多啦。我肯定你已经爱上了学习生成器。一定要记住，想要完全掌握这个概念，你只有使用它。确保你按照这个模式，并在生成器对你有意义的任何时候都使用它。你绝对不会失望的！
