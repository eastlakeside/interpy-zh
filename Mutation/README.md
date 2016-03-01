# 对象变动(Mutation)

Python中可变(**mutable**)与不可变(**immutable**)的数据类型让新手很是头痛。简单的说，可变(mutable)意味着"可以被改动"，而不可变(immutable)的意思是“常量(constant)”。想把脑筋转动起来吗？考虑下这个例子：

```python
foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']
print(foo)
# Output: ['hi', 'bye']
```

刚刚发生了什么？我们预期的不是那样！我们期望看到是这样的：

```python
foo = ['hi']
print(foo)
# Output: ['hi']

bar = foo
bar += ['bye']

print(foo)
# Output: ['hi']

print(bar)
# Output: ['hi', 'bye']
```

这不是一个bug。这是对象可变性(**mutability**)在作怪。每当你将一个变量赋值为另一个可变类型的变量时，对这个数据的任意改动会同时反映到这两个变量上去。新变量只不过是老变量的一个别名而已。这个情况只是针对可变数据类型。下面的函数和可变数据类型让你一下就明白了：

```python
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)
# Output: [1, 2, 3]
```
你可能预期它表现的不是这样子。你可能希望，当你调用```add_to```时，有一个新的列表被创建，就像这样：

```python
def add_to(num, target=[]):
    target.append(num)
    return target

add_to(1)
# Output: [1]

add_to(2)
# Output: [2]

add_to(3)
# Output: [3]
```
啊哈！这次又没有达到预期，是列表的可变性在作怪。在Python中当函数被定义时，默认参数只会运算一次，而不是每次被调用时都会重新运算。你应该永远不要定义可变类型的默认参数，除非你知道你正在做什么。你应该像这样做：

```python
def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target
``` 
现在每当你在调用这个函数不传入```target```参数的时候，一个新的列表会被创建。举个例子：

```python
add_to(42)
# Output: [42]

add_to(42)
# Output: [42]

add_to(42)
# Output: [42]
```
