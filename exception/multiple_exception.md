# 处理多个异常

我们可以使用三个方法来处理多个异常。第一个方法需要把所有可能发生的异常放到一个元组里。像这样：

```python
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
```

另外一种方式是对每个单独的异常在单独的except语句块中处理。我们想要多少个except语句块都可以。这里是个例子：
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

上面这个方式中，如果异常没有被第一个except语句块处理，那么它也许被下一个语句块处理，或者根本不会被处理。现在，最后一种方式会捕获**所有**异常：
```python
try:
    file = open('test.txt', 'rb')
except Exception:
    # Some logging if you want
    raise
```

当你不知道你的程序会抛出什么样的异常时，上面的方式可能非常有帮助。
