# 容器(```Collections```)

Python附带一个模块，它包含许多容器数据类型，名字叫作```collections```。我们将讨论它的作用和用法。

我们将讨论的是：

* defaultdict
* counter
* deque
* namedtuple
* enum.Enum (包含在Python 3.4以上)

# defaultdict

我个人使用```defaultdict```较多，与```dict```类型不同，你不需要检查**key**是否存在，所以我们能这样做：

```python
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favourite_colours = defaultdict(list)

for name, colour in colours:
    favourite_colours[name].append(colour)

print(favourite_colours)
```

## 运行输出
```python
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })
```
另一种重要的是例子就是：当你在一个字典中对一个键进行嵌套赋值时，如果这个键不存在，会触发```keyError```异常。 ```defaultdict```允许我们用一个聪明的方式绕过这个问题。
 首先我分享一个使用```dict```触发```KeyError```的例子，然后提供一个使用```defaultdict```的解决方案。

**问题**：

```python
some_dict = {}
some_dict['colours']['favourite'] = "yellow"

## 异常输出：KeyError: 'colours'
```

**解决方案**：

```python
import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"

## 运行正常
```

你可以用```json.dumps```打印出```some_dict```，例如：
```python
import json
print(json.dumps(some_dict))

## 输出: {"colours": {"favourite": "yellow"}}
```

# counter

Counter是一个计数器，它可以帮助我们针对某项数据进行计数。比如它可以用来计算每个人喜欢多少种颜色：

```python
from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)

favs = Counter(name for name, colour in colours)
print(favs)

## 输出:
## Counter({
##     'Yasoob': 2,
##     'Ali': 2,
##     'Arham': 1,
##     'Ahmed': 1
##  })
```
我们也可以在利用它统计一个文件，例如：

```python
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)
```

# deque

deque提供了一个双端队列，你可以从头/尾两端添加或删除元素。要想使用它，首先我们要从```collections```中导入```deque```模块：

```python
from collections import deque
```
现在，你可以创建一个```deque```对象。

```python
d = deque()
```
它的用法就像python的```list```，并且提供了类似的方法，例如：

```python
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))

## 输出: 3

print(d[0])

## 输出: '1'

print(d[-1])

## 输出: '3'
```

你可以从两端取出(pop)数据：

```python
d = deque(range(5))
print(len(d))

## 输出: 5

d.popleft()

## 输出: 0

d.pop()

## 输出: 4

print(d)

## 输出: deque([1, 2, 3])
```

我们也可以限制这个列表的大小，当超出你设定的限制时，数据会从对队列另一端被挤出去(pop)。  
最好的解释是给出一个例子：

```python
d = deque(maxlen=30)
```
现在当你插入30条数据时，最左边一端的数据将从队列中删除。

你还可以从任一端扩展这个队列中的数据：

```python
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)

## 输出: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
```


# namedtuple

您可能已经熟悉元组。  
一个元组是一个不可变的列表，你可以存储一个数据的序列，它和命名元组(```namedtuples```)非常像，但有几个关键的不同。  
主要相似点是都不像列表，你不能修改元组中的数据。为了获取元组中的数据，你需要使用整数作为索引：


```python
man = ('Ali', 30)
print(man[0])

## 输出: Ali
```


嗯，那```namedtuples```是什么呢？它把元组变成一个针对简单任务的容器。你不必使用整数索引来访问一个```namedtuples```的数据。你可以像字典(```dict```)一样访问```namedtuples```，但```namedtuples```是不可变的。

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)

## 输出: Animal(name='perry', age=31, type='cat')

print(perry.name)

## 输出: 'perry'
```

现在你可以看到，我们可以用名字来访问```namedtuple```中的数据。我们再继续分析它。一个命名元组(```namedtuple```)有两个必需的参数。它们是元组名称和字段名称。

在上面的例子中，我们的元组名称是```Animal```，字段名称是'name'，'age'和'type'。  
`namedtuple`让你的元组变得**自文档**了。你只要看一眼就很容易理解代码是做什么的。  
你也不必使用整数索引来访问一个命名元组，这让你的代码更易于维护。  
而且，**```namedtuple```的每个实例没有对象字典**，所以它们很轻量，与普通的元组比，并不需要更多的内存。这使得它们比字典更快。

然而，要记住它是一个元组，属性值在```namedtuple```中是不可变的，所以下面的代码不能工作：

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
perry.age = 42

## 输出:
## Traceback (most recent call last):
##     File "", line 1, in
## AttributeError: can't set attribute
```

你应该使用命名元组来让代码**自文档**，**它们向后兼容于普通的元组**，这意味着你可以既使用整数索引，也可以使用名称来访问```namedtuple```：

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])

## 输出: perry
```

最后，你可以将一个命名元组转换为字典，方法如下：

```python
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())

## 输出: OrderedDict([('name', 'Perry'), ('age', 31), ...
```


# enum.Enum (Python 3.4+)

另一个有用的容器是枚举对象，它属于```enum```模块，存在于Python 3.4以上版本中（同时作为一个独立的PyPI包```enum34```供老版本使用）。Enums(枚举类型)基本上是一种组织各种东西的方式。

让我们回顾一下上一个'Animal'命名元组的例子。  
它有一个type字段，问题是，type是一个字符串。  
那么问题来了，万一程序员输入了```Cat```，因为他按到了Shift键，或者输入了'CAT'，甚至'kitten'？

枚举可以帮助我们避免这个问题，通过不使用字符串。考虑以下这个例子：

```python
from collections import namedtuple
from enum import Enum

class Species(Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # 依次类推

    # 但我们并不想关心同一物种的年龄，所以我们可以使用一个别名
    kitten = 1  # (译者注：幼小的猫咪)
    puppy = 2   # (译者注：幼小的狗狗)

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)
```

## 现在，我们进行一些测试：
```python
>>> charlie.type == tom.type
True
>>> charlie.type
<Species.cat: 1>
```

这样就没那么容易错误，我们必须更明确，而且我们应该只使用定义后的枚举类型。

有三种方法访问枚举数据，例如以下方法都可以获取到'cat'的值：

```python
Species(1)
Species['cat']
Species.cat
```

这只是一个快速浏览```collections```模块的介绍，建议你阅读本文最后的官方文档。