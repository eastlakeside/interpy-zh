# 字典推导式（```dict``` comprehensions）

字典推导和列表推导的使用方法是类似的。这里有个我最近发现的例子：
```python
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}

# mcase_frequency == {'a': 17, 'z': 3, 'b': 34}
```

在上面的例子中我们把同一个字母但不同大小写的值合并起来了。  

就我个人来说没有大量使用字典推导式。

你还可以快速对换一个字典的键和值：
```python
{v: k for k, v in some_dict.items()}
```
