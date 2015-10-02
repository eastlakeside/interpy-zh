# 收集器(Collections)
Python附带一个模块，它包含许多容器数据类型，名字叫作collections。我们将讨论它的作用和用法。

我们将讨论的是：

* defaultdict
* counter
* deque
* namedtuple
* enum.Enum (包含在Python 3.4以上)

# defaultdict

我个人使用```defaultdict```较多，与```dict```类型不同，你不需要检查**key**是否存在，所以我们能这样做：
```
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
```
# defaultdict(<type 'list'>,
#    {'Arham': ['Green'],
#     'Yasoob': ['Yellow', 'Red'],
#     'Ahmed': ['Silver'],
#     'Ali': ['Blue', 'Black']
# })
```
另一种重要的是例子就是：当你在**字典(dict)**中用**列表(list)**作key，如果**key**不存在，会返回```keyError```异常。 ```defaultdict```允许我们用一个聪明的方式绕过这个问题。
 首先我分享一个例子，使用```dict```获得```KeyError```，然后提供一个使用```defaultdict```的解决方案。

问题：

```
some_dict = {}
some_dict['colours']['favourite'] = "yellow"
```

## 异常输出：KeyError: 'colours'
解决方案：

```
import collections
tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"
```
## 工作正常
你可以用```json.dumps```打印出```some_dict```，例如：
```
import json
print(json.dumps(some_dict))
```
## 输出: {"colours": {"favourite": "yellow"}}
# counter

Counter是一个计数器，它可以帮助我们针对某项数据进行计数。比如它可以用来计算每个人喜欢多少种颜色：

```
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
```
## 输出:
```
Counter({
    'Yasoob': 2,
    'Ali': 2,
    'Arham': 1,
    'Ahmed': 1
 })
```
我们也可以在利用它统计一个文件，例如：

```
with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)
```

# deque

deque提供了一个双端队列，你可以从头/尾两端添加或删除元素。要想使用它，首先我们要从```collections```中导入```deque```模块：

```
from collections import deque
```
现在，你可以创建一个```deque```对象。

```
d = deque()
```
它的用法就像python的```list```，并且提供了类似的方法，例如：

```
d = deque()
d.append('1')
d.append('2')
d.append('3')

print(len(d))
```

## 输出: 3

```
print(d[0])
```

## 输出: '1'

```
print(d[-1])
```
## 输出: '3'
你可以从两端取出(pop)数据：

```
d = deque(range(5))
print(len(d))
```
## 输出: 5

```
d.popleft()
```
## 输出: 0

```
d.pop()
```
## 输出: 4

```
print(d)
```
# 输出: deque([1, 2, 3])

我们也可以限制这个列表的大小，当超出你设定的限制时，数据会从对端流出去(pop)。
最好的解释是给出一个例子：

```
d = deque(maxlen=30)
```
现在当你插入30条数据时，最左边(最早？)的数据将从队列中删除。

你还可以从任一端扩展这个队列中的数据：

```
d = deque([1,2,3,4,5])
d.extendleft([0])
d.extend([6,7,8])
print(d)
```

## 输出: deque([0, 1, 2, 3, 4, 5, 6, 7, 8])
这只是一个快速浏览```collections```模块的介绍，建议你阅读本文最后的官方文档。

# namedtuple

You might already be acquainted with tuples. A tuple is basically a immutable list which allows you to store a sequence of values separated by commas. They are just like lists but have a few key differences. The major one is that unlike lists, you can not reassign an item in a tuple. In order to access the value in a tuple you use integer indexes like:

man = ('Ali', 30)
print(man[0])
# Output: Ali
Well, so now what are namedtuples? They turn tuples into convenient containers for simple tasks. With namedtuples you don't have to use integer indexes for accessing members of a tuple. You can think of namedtuples like dictionaries but unlike dictionaries they are immutable.

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(perry)
# Output: Animal(name='perry', age=31, type='cat')

print(perry.name)
# Output: 'perry'
You can now see that we can access members of a tuple just by their name using a .. Let's dissect it a little more. A named tuple has two required arguments. They are the tuple name and the tuple field_names. In the above example our tuple name was 'Animal' and the tuple field_names were 'name', 'age' and 'cat'. Namedtuple makes your tuples self-document. You can easily understand what is going on by having a quick glance at your code. And as you are not bound to use integer indexes to access members of a tuple, it makes it more easy to maintain your code. Moreover, as `namedtuple` instances do not have per-instance dictionaries, they are lightweight and require no more memory than regular tuples. This makes them faster than dictionaries. However, do remember that as with tuples, attributes in namedtuples are immutable. It means that this would not work:

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
perry.age = 42

# Output: Traceback (most recent call last):
#            File "", line 1, in
#         AttributeError: can't set attribute
You should use named tuples to make your code self-documenting. They are backwards compatible with normal tuples. It means that you can use integer indexes with namedtuples as well:

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
print(perry[0])
# Output: perry
Last but not the least, you can convert a namedtuple to a dictionary. Like this:

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type="cat")
print(perry._asdict())
# Output: OrderedDict([('name', 'Perry'), ('age', 31), ...
enum.Enum (Python 3.4+)

Another useful collection is the enum object. It is available in the enum module, in Python 3.4 and up (also available as a backport in PyPI named enum34.) Enums (enumerated type) are basically a way to organize various things.

Let’s consider the Animal namedtuple from the last example. It had a type field. The problem is, the type was a string. This poses some problems for us. What if the user types in Cat because they held the Shift key? Or CAT? Or kitten?

Enumerations can help us avoid this problem, by not using strings. Consider this example:

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
    # The list goes on and on...

    # But we don't really care about age, so we can use an alias.
    kitten = 1
    puppy = 2

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="Perry", age=31, type=Species.cat)
drogon = Animal(name="Drogon", age=4, type=Species.dragon)
tom = Animal(name="Tom", age=75, type=Species.cat)
charlie = Animal(name="Charlie", age=2, type=Species.kitten)

# And now, some tests.
>>> charlie.type == tom.type
True
>>> charlie.type
<Species.cat: 1>
This is much less error-prone. We have to be specific, and we should use only the enumeration to name types.

There are three ways to access enumeration members. For example, all three methods will get you the value for cat:

Species(1)
Species['cat']
Species.cat