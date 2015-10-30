# try/else从句

我们常常想让一些代码在没有异常触发的情况下执行。这可以很轻松地通过使用一个else从句来达到。有人也许问了：为什么，如果你只是想让一些代码如果没有异常触发的情况下执行，你为啥不直接把代码放在try里面呢？回答是，那样的话这段代码中的任意异常都还是会被try捕获，而你并不一定想要那样。大多数人并不使用它，而且坦率地讲我自己也没有大范围使用。这里是个例子：
```python
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # any code that should only run if no exception occurs in the try,
    # but for which exceptions should NOT be caught
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs.
# This would be printed in every case.
```
else从句只会在没有异常的情况下执行，而且它会在finally语句之前执行。
