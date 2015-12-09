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
这里有一篇[Caktus Group的不错的文章](https://www.caktusgroup.com/blog/2015/06/08/testing-client-side-applications-django-post-mortem/)，在其中他们发现一个Django框架的由lru_cache导致的bug。读起来很有意思。一定要打开去看一下。
