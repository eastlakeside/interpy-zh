# 异常

异常处理是一种艺术，一旦你掌握，会授予你无穷的力量。我将要给你展示我们能处理异常的一些方式。

最基本的术语里我们知道了try/except从句。可能触发异常产生的代码会放到try语句块里，而处理异常的代码会在except语句块里实现。这是一个简单的例子：

```python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
```

上面的例子里，我们仅仅在处理一个IOError的异常。大部分初学者还不知道的是，我们可以处理多个异常。