# ```Filter```

顾名思义，```filter```过滤列表中的元素，并且返回一个由所有符合要求的元素所构成的列表，```符合要求```即函数映射到该元素时返回值为True. 这里是一个简短的例子：

```python
number_list = range(-5, 5)
less_than_zero = filter(lambda x: x < 0, number_list)
print(list(less_than_zero))  
# 译者注：上面print时，加了list转换，是为了python2/3的兼容性
#        在python2中filter直接返回列表，但在python3中返回迭代器
#        因此为了兼容python3, 需要list转换一下

# Output: [-5, -4, -3, -2, -1]
```

这个```filter```类似于一个```for```循环，但它是一个内置函数，并且更快。

注意：如果```map```和```filter```对你来说看起来并不优雅的话，那么你可以看看另外一章：列表/字典/元组推导式。
> 译者注：大部分情况下推导式的可读性更好
