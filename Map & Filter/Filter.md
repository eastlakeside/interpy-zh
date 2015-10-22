# Filter

顾名思义，filter能创建一个列表，其中每个元素都是对一个函数能返回True. 这里是一个简短的例子：
```python
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]
```

这个filter类似于一个for循环，但它是一个内置函数，并且更快。

注意：如果map和filter对你来说看起来并不优雅的话，那么你可以看看另外一章：列表/字典/元组推导式。(译者注：大部分情况下推导式的可读性更好)
