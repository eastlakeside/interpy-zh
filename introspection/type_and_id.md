# type和id

函数```type()```返回一个对象的类型。举个例子：


```python
print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>
```

函数```id()```返回任意不同种类对象的唯一ID，举个例子：

```python
name = "Yasoob"
print(id(name))
# Output: 139972439030304
```