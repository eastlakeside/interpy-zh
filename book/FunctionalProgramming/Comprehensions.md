---
parent: 函数式编程
nav_order: 5
---


# 推导式(解析式)

推导式（`comprehensions`）（在中文又称解析式）是 Python 的一种独有特性，如果我被迫离开了它，我会非常想念。推导式是可以从一个数据序列构建另一个新的数据序列的结构体。共有三种推导，在Python 2和3中都有支持：

- 列表（```list```）推导式
- 字典（```dict```）推导式
- 集合（```set```）推导式

我们将一一进行讨论。一旦你知道了使用列表推导式的诀窍，你就能轻易使用任意一种推导式了。

# 列表推导式（```list``` comprehensions）

列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。  
它的结构是在一个中括号里包含一个表达式，然后是一个 ```for``` 语句，然后是0个或多个 ```for``` 或者 ```if``` 语句。那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以 ```if``` 和 ```for``` 语句为上下文的表达式运行完成之后产生。

## 规范

```python
variable = [out_exp for out_exp in input_list if out_exp == 2]
```

这里是另外一个简明例子:

```python
multiples = [i for i in range(30) if i % 3 is 0]
print(multiples)
# Output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
```

这将对快速生成列表非常有用。  
有些人甚至更喜欢使用它而不是 ```filter``` 函数。  
列表推导式在有些情况下超赞，特别是当你需要使用 ```for``` 循环来生成一个新列表。举个例子，你通常会这样做：

```python
squared = []
for x in range(10):
    squared.append(x**2)
```

你可以使用列表推导式来简化它，就像这样：

```python
squared = [x**2 for x in range(10)]
```


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

# 集合推导式（```set``` comprehensions）

它们跟列表推导式也是类似的。 唯一的区别在于它们使用大括号```{}```。 举个例子：

```python
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}
```
