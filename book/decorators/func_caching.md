---
parent: 装饰器
nav_order: 4
---

# 函数缓存（Function caching）

函数缓存允许我们将一个函数对于给定参数的返回值缓存起来。  
当一个 I/O 密集的函数被频繁使用相同的参数调用的时候，函数缓存可以节约时间。  
在 Python 3.2 版本以前我们只有写一个自定义的实现。在 Python 3.2 以后版本，有个 ```lru_cache``` 的装饰器，允许我们将一个函数的返回值快速地缓存或取消缓存。

我们来看看，Python 3.2 前后的版本分别如何使用它。

# Python 3.2及以后版本

我们来实现一个斐波那契计算器，并使用 ```lru_cache```。

```python
from functools import lru_cache

@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

>>> print([fib(n) for n in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

那个 ```maxsize``` 参数是告诉 ```lru_cache```，最多缓存最近多少个返回值。

我们也可以轻松地对返回值清空缓存，通过这样：

```python
fib.cache_clear()
```

# Python 2系列版本

你可以创建任意种类的缓存机制，有若干种方式来达到相同的效果，这完全取决于你的需要。
这里是一个一般的缓存：

```python
from functools import wraps

def memoize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

@memoize
def fibonacci(n):
    if n < 2: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci(25)
```

这里有一篇 [Caktus Group 的不错的文章](https://www.caktusgroup.com/blog/2015/06/08/testing-client-side-applications-django-post-mortem/)，在其中他们发现一个 Django 框架的由 lru_cache 导致的 bug。读起来很有意思。一定要打开去看一下。
