---
parent: 语法
nav_order: 1
---

# 异常

异常处理是一种艺术，一旦你掌握，会授予你无穷的力量。我将要向你展示我们能处理异常的一些方式。

最基本的术语里我们知道了 ```try/except``` 从句。可能触发异常产生的代码会放到 ```try``` 语句块里，而处理异常的代码会在 ```except``` 语句块里实现。这是一个简单的例子：

```python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
```

上面的例子里，我们仅仅在处理一个 ```IOError``` 的异常。大部分初学者还不知道的是，我们可以处理多个异常。


# 处理多个异常

我们可以使用三种方法来处理多个异常。

第一种方法需要把所有可能发生的异常放到一个元组里。像这样：

```python
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
```

另外一种方式是对每个单独的异常在单独的 ```except``` 语句块中处理。我们想要多少个 ```except``` 语句块都可以。这里是个例子：

```python
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e
```

上面这个方式中，如果异常没有被第一个 ```except``` 语句块处理，那么它也许被下一个语句块处理，或者根本不会被处理。

现在，最后一种方式会捕获**所有**异常：

```python
try:
    file = open('test.txt', 'rb')
except Exception:
    # 打印一些异常日志，如果你想要的话
    raise
```

当你不知道你的程序会抛出什么样的异常时，上面的方式可能非常有帮助。


# ```finally``` 从句

我们把我们的主程序代码包裹进了 ```try``` 从句。然后我们把一些代码包裹进一个 ```except``` 从句，它会在 ```try``` 从句中的代码触发异常时执行。

在下面的例子中，我们还会使用第三个从句，那就是 ```finally``` 从句。包裹到 ```finally``` 从句中的代码不管异常是否触发都将会被执行。这可以被用来在脚本执行之后做清理工作。这里是个简单的例子：

```python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# Output: An IOError occurred. No such file or directory
# This would be printed whether or not an exception occurred!
```

# ```try/else``` 从句

我们常常想在没有触发异常的时候执行一些代码。这可以很轻松地通过一个 ```else``` 从句来达到。

有人也许问了：如果你只是想让一些代码在没有触发异常的情况下执行，为啥你不直接把代码放在 ```try``` 里面呢？  
回答是，那样的话这段代码中的任意异常都还是会被 ```try``` 捕获，而你并不一定想要那样。

大多数人并不使用 ```else``` 从句，而且坦率地讲我自己也没有大范围使用。这里是个例子：

```python
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs.
# This would be printed in every case.
```

```else``` 从句只会在没有异常的情况下执行，而且它会在 ```finally``` 语句之前执行。
