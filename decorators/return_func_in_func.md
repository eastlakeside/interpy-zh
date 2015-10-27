# 从函数中返回函数

其实并不需要在一个函数里去执行另一个函数，我们也可以将其作为输出返回出来：

```python
def hi(name="yasoob"):
    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "yasoob":
        return greet
    else:
        return welcome

a = hi()
print(a)
#outputs: <function greet at 0x7f2143c01500>

#上面清晰地展示了`a`现在指向到hi()函数中的greet()函数
#现在试试这个

print(a())
#outputs: now you are in the greet() function
```

再次看看这个代码。在```if/else```语句中我们返回```greet```和```welcome```，而不是```greet()```和```welcome()```。为什么那样？这是因为当你把一对小括号放在后面，这个函数就会执行；然而如果你不放括号在它后面，那它可以被到处传递，并且可以赋值给别的变量而不去执行它。

你明白了吗？让我再稍微多解释点细节。

当我们写下```a = hi()```，```hi()```会被执行，而由于```name```参数默认是*yasoob*，所以函数```greet```被返回了。如果我们把语句改为```a = hi(name = "ali")```，那么```welcome```函数将被返回。我们还可以打印出```hi()()```，这会输出*now you are in the greet() function*。
