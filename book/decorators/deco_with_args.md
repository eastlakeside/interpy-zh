---
parent: 装饰器
nav_order: 3
---

# 带参数的装饰器

来想想这个问题，难道 ```@wraps``` 不也是个装饰器吗？但是，它接收一个参数，就像任何普通的函数能做的那样。那么，为什么我们不也那样做呢？

这是因为，当你使用 ```@my_decorator``` 语法时，你是在应用一个以单个函数作为参数的一个包裹函数。记住，Python里每个东西都是一个对象，而且这包括函数！记住了这些，我们可以编写一下能返回一个包裹函数的函数。


# 在函数中嵌入装饰器

我们回到日志的例子，并创建一个包裹函数，能让我们指定一个用于输出的日志文件。

```python
from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
```


# 装饰器类

现在我们有了能用于正式环境的 ```logit``` 装饰器，但当我们的应用的某些部分还比较脆弱时，异常也许是需要更紧急关注的事情。比方说有时你只想打日志到一个文件。而有时你想把引起你注意的问题发送到一个email，同时也保留日志，留个记录。这是一个使用继承的场景，但目前为止我们只看到过用来构建装饰器的函数。

幸运的是，类也可以用来构建装饰器。那我们现在以一个类而不是一个函数的方式，来重新构建 ```logit```。

```python
class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # 打开logfile并写入
        with open(self._logfile, 'a') as opened_file:
            # 现在将日志打到指定的文件
            opened_file.write(log_string + '\n')
        # 现在，发送一个通知
        self.notify()

        # return base func
        return self.func(*args)



    def notify(self):
        # logit只打日志，不做别的
        pass
```

这个实现有一个附加优势，在于比嵌套函数的方式更加整洁，而且包裹一个函数还是使用跟以前一样的语法：

```python
logit._logfile = 'out2.log' # 如果需要修改log文件参数
@logit
def myfunc1():
    pass

myfunc1()
# 输出: myfunc1 was called
```

现在，我们给```logit```创建子类，来添加email的功能(虽然email这个话题不会在这里展开)。

```python
class email_logit(logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, func, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(func, *args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass
```

从现在起，```@email_logit``` 将会和 ```@logit``` 产生同样的效果，但是在打日志的基础上，还会多发送一封邮件给管理员。

```python
email_logit._logfile = 'out3.log' # 如果需要修改log文件参数
@email_logit
def myfunc2():
    pass

myfunc2()
# 输出: myfunc2 was called
```
