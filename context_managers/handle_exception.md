# 处理异常

我们还没有谈到```__exit__```方法的这三个参数：```type```, ```value```和```traceback```。  
在第4步和第6步之间，如果发生异常，Python会将异常的```type```,```value```和```traceback```传递给```__exit__```方法。  
它让```__exit__```方法来决定如何关闭文件以及是否需要其他步骤。在我们的案例中，我们并没有注意它们。

那如果我们的文件对象抛出一个异常呢？万一我们尝试访问文件对象的一个不支持的方法。举个例子：

```python
with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function('Hola!')
```

我们来列一下，当异常发生时，```with```语句会采取哪些步骤。
1. 它把异常的```type```,```value```和```traceback```传递给```__exit__```方法
2. 它让```__exit__```方法来处理异常
3. 如果```__exit__```返回的是True，那么这个异常就被优雅地处理了。
4. 如果```__exit__```返回的是True以外的任何东西，那么这个异常将被```with```语句抛出。

在我们的案例中，```__exit__```方法返回的是```None```(如果没有```return```语句那么方法会返回```None```)。因此，```with```语句抛出了那个异常。

```python
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'file' object has no attribute 'undefined_function'
```

我们尝试下在```__exit__```方法中处理异常：
```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        print("Exception has been handled")
        self.file_obj.close()
        return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Output: Exception has been handled
```

我们的```__exit__```方法返回了```True```,因此没有异常会被```with```语句抛出。

这还不是实现上下文管理器的唯一方式。还有一种方式，我们会在下一节中一起看看。
