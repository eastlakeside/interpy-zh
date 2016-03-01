# 18. 一行式
本章节,我将向大家展示一些一行式的Python命令，这些程序将对你非常有帮助。

**简易Web Server**

你是否想过通过网络快速共享文件？好消息，Python为你提供了这样的功能。进入到你要共享文件的目录下并在命令行中运行下面的代码：

```sh
    # Python 2
    python -m SimpleHTTPServer

    # Python 3
    python -m http.server
```

**漂亮的打印**

你可以在Python REPL漂亮的打印出列表和字典。这里是相关的代码：

```python
    from pprint import pprint

    my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
    pprint(my_dict)

```
这种方法在字典上更为有效。此外，如果你想快速漂亮的从文件打印出json数据，那么你可以这么做：
```sh
    cat file.json | python -m json.tool
```

**脚本性能分析**
这可能在定位你的脚本中的性能瓶颈时，会非常奏效：

```sh
    python -m cProfile my_script.py
```
备注：```cProfile```是一个比```profile```更快的实现，因为它是用c写的

**CSV转换为json**

在命令行执行这条指令
```sh
    python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
```
确保更换```csv_file.csv```为你想要转换的csv文件

**列表辗平**

您可以通过使用```itertools```包中的```itertools.chain.from_iterable```轻松快速的辗平一个列表。下面是一个简单的例子：
```python
    a_list = [[1, 2], [3, 4], [5, 6]]
    print(list(itertools.chain.from_iterable(a_list)))
    # Output: [1, 2, 3, 4, 5, 6]

    # or
    print(list(itertools.chain(*a_list)))
    # Output: [1, 2, 3, 4, 5, 6]
```

**一行式的构造器**

避免类初始化时大量重复的赋值语句
```python
    class A(object):
        def __init__(self, a, b, c, d, e, f):
            self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})
```
更多的一行方法请参考[Python官方文档](https://wiki.python.org/moin/Powerful%20Python%20One-Liners)。


