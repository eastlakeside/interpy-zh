# 集合推导式（```set``` comprehensions）

它们跟列表推导式也是类似的。 唯一的区别在于它们使用大括号```{}```。 举个例子：
```python
squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}
```