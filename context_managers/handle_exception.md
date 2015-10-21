# 处理异常

我们还没有谈到__exit__方法的这三个参数：typle, value和traceback。在第4步和第6步之间，如果发生异常，Python会将异常的type,value和traceback传递到__exit__方法。它让__exit__方法来决定如何关闭文件以及是否需要其他步骤。在我们的案例中，我们并没有注意它们。

那如果我们的文件对象抛出一个异常呢？万一我们尝试访问文件对象的一个不支持的方法。举个例子：
```
with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function('Hola!')
```

我们来列一下，当异常发生时，with语句会采取哪些步骤。
1. 它把异常的type,value和traceback传递给__exit__方法
2. 它让__exit__方法来处理异常
3. 


It passes the type, value and traceback of the error to the __exit__ method.
It allows the __exit__ method to handle the exception.
If __exit__ returns True then the exception was gracefully handled.
If anything else than True is returned by __exit__ method then the exception is raised by with statement.
In our case the __exit__ method returns None (when no return statement is encountered then the method returns None). Therefore, with statement raises the exception.

Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
AttributeError: 'file' object has no attribute 'undefined_function'
Let’s try handling the exception in the __exit__ method:

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
Our __exit__ method returned True, therefore no exception was raised by the with statement.

This is not the only way to implement context managers. There is another way and we will be looking at it in this next section.