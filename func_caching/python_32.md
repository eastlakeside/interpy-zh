# Python 3.2及以后版本

我们来实现一个斐波那契计算器，并使用```lru_cache```。

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

那个```maxsize```参数是告诉```lru_cache```，最多缓存最近多少个返回值。

我们也可以轻松地对返回值清空缓存，通过这样：

```python
fib.cache_clear()
```

