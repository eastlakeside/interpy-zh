# 使用 ```*args``` 和 ```**kwargs``` 来调用一个函数

那我们来看看怎样使用```*args```和```**kwargs``` 来调用一个函数。
现在假设你有这样一个小函数：
```
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
```

现在你可以使用```*args```或```**kwargs```来给这个小函数传递参数。 下面就是如何来做到：
```
# first with *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# now with **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```

### 标准参数与```*args、**kwargs```在使用时的顺序

那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
```
some_func(fargs, *args, **kwargs)
```