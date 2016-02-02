# 使用 ```*args``` 和 ```**kwargs``` 来调用函数

那现在我们将看到怎样使用```*args```和```**kwargs``` 来调用一个函数。
 假设，你有这样一个小函数：
```python
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)
```

你可以使用```*args```或```**kwargs```来给这个小函数传递参数。 
下面是怎样做：
```python
# 首先使用 *args
>>> args = ("two", 3, 5)
>>> test_args_kwargs(*args)
arg1: two
arg2: 3
arg3: 5

# 现在使用 **kwargs:
>>> kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
>>> test_args_kwargs(**kwargs)
arg1: 5
arg2: two
arg3: 3
```

### 标准参数与```*args、**kwargs```在使用时的顺序

那么如果你想在函数里同时使用所有这三种参数， 顺序是这样的：
```python
some_func(fargs, *args, **kwargs)
```