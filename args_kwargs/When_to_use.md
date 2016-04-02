# 什么时候使用它们？

这还真的要看你的需求而定。

最常见的用例是在写函数装饰器的时候（会在另一章里讨论）。

此外它也可以用来做猴子补丁(monkey patching)。猴子补丁的意思是在程序运行时(runtime)修改某些代码。 打个比方，你有一个类，里面有个叫```get_info```的函数会调用一个API并返回相应的数据。如果我们想测试它，可以把API调用替换成一些测试数据。例如：
```python
import someclass

def get_info(self, *args):
    return "Test data"

someclass.get_info = get_info
```

我敢肯定你也可以想象到一些其他的用例。


