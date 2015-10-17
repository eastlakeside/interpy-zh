# Python 3.2及以后版本

我们来实现一个斐波那契计算器，并使用lru_cache。

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
The maxsize argument tells lru_cache about how many recent return values to cache.

We can easily uncache the return values as well by using:

fib.cache_clear()
