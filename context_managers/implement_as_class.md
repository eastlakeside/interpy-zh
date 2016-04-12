# 基于类的实现

一个上下文管理器的类，最起码要定义```__enter__```和```__exit__```方法。  
让我们来构造我们自己的开启文件的上下文管理器，并学习下基础知识。

```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
```

通过定义```__enter__```和```__exit__```方法，我们可以在```with```语句里使用它。我们来试试：

```python
with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
```    

我们的```__exit__```函数接受三个参数。这些参数对于每个上下文管理器类中的```__exit__```方法都是必须的。我们来谈谈在底层都发生了什么。

1. ```with```语句先暂存了```File```类的```__exit__```方法
2. 然后它调用```File```类的```__enter__```方法
3. ```__enter__```方法打开文件并返回给```with```语句
4. 打开的文件句柄被传递给```opened_file```参数
5. 我们使用```.write()```来写文件
6. ```with```语句调用之前暂存的```__exit__```方法
7. ```__exit__```方法关闭了文件
