---
parent: 语法
nav_order: 4
---

# Global 和 Return

你也许遇到过, python中一些函数在最尾部有一个 ```return``` 关键字。你知道它是干嘛吗？它和其他语言的 ```return``` 类似。我们来检查下这个小函数：

```python
def add(value1, value2):
    return value1 + value2

result = add(3, 5)
print(result)
# Output: 8
```

上面这个函数将两个值作为输入，然后输出它们相加之和。我们也可以这样做：

```python
def add(value1,value2):
    global result
    result = value1 + value2

add(3,5)
print(result)
# Output: 8
```

那首先我们来谈谈第一段也就是包含 ```return``` 关键字的代码。那个函数把值赋给了调用它的变量（也就是例子中的result变量）。  
大多数境况下，你并不需要使用 ```global``` 关键字。然而我们也来检查下另外一段也就是包含 ```global``` 关键字的代码。
那个函数生成了一个 ```global```（全局）变量 ```result```。

```global``` 在这的意思是什么？```global``` 变量意味着我们可以在函数以外的区域都能访问这个变量。让我们通过一个例子来证明它：

```python
# 首先，是没有使用global变量
def add(value1, value2):
    result = value1 + value2

add(2, 4)
print(result)

# Oh 糟了，我们遇到异常了。为什么会这样？
# python解释器报错说没有一个叫result的变量。
# 这是因为result变量只能在创建它的函数内部才允许访问，除非它是全局的(global)。
Traceback (most recent call last):
  File "", line 1, in
    result
NameError: name 'result' is not defined

# 现在我们运行相同的代码，不过是在将result变量设为global之后
def add(value1, value2):
    global result
    result = value1 + value2

add(2, 4)
print(result)
6
```

如我们所愿，在第二次运行时没有异常了。在实际的编程时，你应该试着避开 ```global``` 关键字，它只会让生活变得艰难，因为它引入了多余的变量到全局作用域了。

# 多个 return 值

那如果你想从一个函数里返回两个变量而不是一个呢？
新手们有若干种方法。最著名的方法，是使用 ```global``` 关键字。让我们看下这个没用的例子：

```python
def profile():
    global name
    global age
    name = "Danny"
    age = 30

profile()
print(name)
# Output: Danny

print(age)
# Output: 30
```

**注意:** 不要试着使用上述方法。重要的事情说三遍，不要试着使用上述方法！不要试着使用上述方法！

有些人试着在函数结束时，返回一个包含多个值的 ```tuple```(元组)，```list```(列表)或者 ```dict```(字典)，来解决这个问题。这是一种可行的方式，而且使用起来像一个黑魔法：

```python
def profile():
    name = "Danny"
    age = 30
    return (name, age)

profile_data = profile()
print(profile_data[0])
# Output: Danny

print(profile_data[1])
# Output: 30
```

或者按照更常见的惯例：

```python
def profile():
    name = "Danny"
    age = 30
    return name, age
```

这是一种比列表和字典更好的方式。不要使用 ```global``` 关键字，除非你知道你正在做什么。```global``` 也许在某些场景下是一个更好的选择（但其中大多数情况都不是）。
