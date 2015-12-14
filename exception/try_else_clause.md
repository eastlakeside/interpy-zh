# ```try/else```从句

我们常常想在没有触发异常的时候执行一些代码。这可以很轻松地通过一个```else```从句来达到。

有人也许问了：如果你只是想让一些代码在没有触发异常的情况下执行，为啥你不直接把代码放在```try```里面呢？  
回答是，那样的话这段代码中的任意异常都还是会被```try```捕获，而你并不一定想要那样。

大多数人并不使用```else```从句，而且坦率地讲我自己也没有大范围使用。这里是个例子：

```python
try:
    print('I am sure no exception is going to occur!')
except Exception:
    print('exception')
else:
    # 这里的代码只会在try语句里没有触发异常时运行,
    # 但是这里的异常将 *不会* 被捕获
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs.
# This would be printed in every case.
```

```else```从句只会在没有异常的情况下执行，而且它会在```finally```语句之前执行。
