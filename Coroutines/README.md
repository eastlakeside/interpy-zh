# 23. 协程
Python中的协程和生成器很相似但又稍有不同。主要区别在于：
* 生成器是数据的生产者
* 协程则是数据的消费者

首先我们先来回顾下生成器的创建过程。我们可以这样去创建一个生成器:

```python
    def fib():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a+b
```

然后我们经常在for循环中这样使用它:

```python
    for i in fib():
        print i
```
这样做不仅快而且不会给内存带来压力，因为我们所需要的值都是动态生成的而不是将他们存储在一个列表中。更概括的说如果现在我们在上面的例子中使用yield便可获得了一个协程。协程会消费掉发送给它的值。Python实现的grep就是个很好的例子：

```python
    def grep(pattern):
        print("Searching for", parttern)
        while True:
            line = (yield)
            if pattern in line:
                print(line) 
```
等等！yield返回了什么？就这样，我们已经把它变成了一个协程。它将不再包含任何初始值，相反要从外部传值给它。我们可以通过send()方法向它传值。这有个例子：

```python
    search = grep('coroutine')
    next(search)
    #output: Searching for coroutine
    search.send("I love you")
    search.send("Don't you love me?")
    search.send("I love coroutine instead!")
    #output: I love coroutine instead!
```
发送的值会被yield接收。我们为什么要运行next()方法呢？这样做正是为了启动一个协程。就像协程中包含的生成器并不是立刻执行，而是通过next()方法来响应send()方法。因此，你必须通过next()方法来执行yield表达式。

我们可以通过调用close()方法来关闭一个协程。像这样：

```python
    search = grep('coroutine')
    search.close()
```
更多协程相关知识的学习大家可以参考David Beazley的这份[精彩演讲](http://www.dabeaz.com/coroutines/Coroutines.pdf)。

