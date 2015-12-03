# 枚举
枚举是Python内置函数。它的用处很难在简单的一行中说明，但是大多数的新人，甚至一些高级程序员都没有意识到它。

它允许我们遍历数据并自动计数，

下面是一个例子：

```python
for counter, value in enumerate(some_list):
    print(counter, value)
```
不只如此，枚举也接受一些可选参数，这使它更有用。
This is not it. enumerate also accepts some optional arguments which make it even more useful.
```
my_list = ['apple', 'banana', 'grapes', 'pear']
for c, value in enumerate(my_list, 1):
    print(c, value)

# 输出:
(1, 'apple')
(2, 'banana')
(3, 'grapes')
(4, 'pear')
```
The optional argument allows us to tell enumerate from where to start the index. You can also create tuples containing the index and list item using a list. Here is an example:
这个可选参数允许我们定制从哪个数字开始枚举，你还可以用来创建包含索引的元组列表，

例如：

```python
my_list = ['apple', 'banana', 'grapes', 'pear']
counter_list = list(enumerate(my_list, 1))
print(counter_list)
# 输出: [(1, 'apple'), (2, 'banana'), (3, 'grapes'), (4, 'pear')]
```
