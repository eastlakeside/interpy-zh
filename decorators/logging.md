# 日志(Logging)

日志是装饰器另一个非常亮眼的领域。这是个例子：
```python
from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(x):
   """Do some math."""
   return x + x


result = addition_func(4)
# Output: addition_func was called
```

我敢肯定已经在思考装饰器的一个其他聪明用法了。

I am sure you are already thinking about some clever uses of decorators.

