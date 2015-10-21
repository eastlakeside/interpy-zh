# 实现成类

一个上下文管理器，起码来说，要定义一个```__enter__```和```__exit__```。让我们来构造我们自己的文件开启的上下文管理器，并学习下基础知识。

class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()
Just by defining __enter__ and __exit__ methods we can use it in a with statement. Let’s try:

with File('demo.txt', 'w') as opened_file:
    opened_file.write('Hola!')
Our __exit__ function accepts three arguments. They are required by every __exit__ method which is a part of a Context Manager class. Let’s talk about what happens under-the-hood.

The with statement stores the __exit__ method of File class.
It calls the __enter__ method of File class.
__enter__ method opens the file and returns it.
the opened file handle is passed to opened_file.
we write to the file using .write()
with statement calls the stored __exit__ method.
the __exit__ method closes the file.