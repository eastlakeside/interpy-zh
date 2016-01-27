# *args 的用法

```*args``` 和 ```**kwargs``` 主要用于函数定义。 你可以将不定数量的参数传递给一个函数。 

这里的不定的意思是：预先并不知道, 函数使用者会传递多少个参数给你, 所以在这个场景下使用这两个关键字。 ```*args``` 是用来发送一个非键值对的可变数量的参数列表给一个函数. 

这里有个例子帮你理解这个概念:


```python
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
```

这会产生如下输出:

```python
first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
```

我希望这解决了你所有的困惑. 那接下来让我们谈谈 ```**kwargs```