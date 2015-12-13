# ```else```从句

```for```循环还有一个```else```从句，我们大多数人并不熟悉。这个```else```从句会在循环正常结束时执行。这意味着，循环没有遇到任何```break```. 一旦你掌握了何时何地使用它，它真的会非常有用。我自己对它真是相见恨晚。

有个常见的构造是跑一个循环，并查找一个元素。如果这个元素被找到了，我们使用```break```来中断这个循环。有两个场景会让循环停下来。
- 第一个是当一个元素被找到，```break```被触发。
- 第二个场景是循环结束。  

现在我们也许想知道其中哪一个，才是导致循环完成的原因。一个方法是先设置一个标记，然后在循环结束时打上标记。另一个是使用```else```从句。

这就是```for/else```循环的基本结构：

```python
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Didn't find anything..
    not_found_in_container()
```
考虑下这个简单的案例，它是我从官方文档里拿来的：
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
```

它会找出2到10之间的数字的因子。现在是趣味环节了。我们可以加上一个附加的else语句块，来抓住质数，并且告诉我们：

```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')
```