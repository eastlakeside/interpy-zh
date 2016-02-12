# 多个return值

那如果你想从一个函数里返回两个变量而不是一个呢？   
新手们有若干种方法。最著名的方法，是使用```global```关键字。让我们看下这个没用的例子：

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
**注意:** 不要试着使用上述方法。重要的事情说三遍，不要试着使用上述方法！


有些人试着在函数结束时，返回一个包含多个值的```tuple```(元组)，```list```(列表)或者```dict```(字典),来解决这个问题。这是一种可行的方式，而且使用起来像一个黑魔法：
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
这是一种比列表和字典更好的方式。不要使用```global```关键字，除非你知道你正在做什么。```global```也许在某些场景下是一个更好的选择（但其中大多数情况都不是）。