# 列表推导式（```list``` comprehensions）

列表推导式（又称列表解析式）提供了一种简明扼要的方法来创建列表。  
它的结构是在一个中括号里包含一个表达式，然后是一个```for```语句，然后是0个或多个```for```或者```if```语句。那个表达式可以是任意的，意思是你可以在列表中放入任意类型的对象。返回结果将是一个新的列表，在这个以```if```和```for```语句为上下文的表达式运行完成之后产生。


### 规范

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
有些人甚至更喜欢使用它而不是```filter```函数。  
列表推导式在有些情况下超赞，特别是当你需要使用```for```循环来生成一个新列表。举个例子，你通常会这样做：
```python
squared = []
for x in range(10):
    squared.append(x**2)
```

你可以使用列表推导式来简化它，就像这样：

```python
squared = [x**2 for x in range(10)]
```