# ```finally```从句

我们把我们的主程序代码包裹进了```try```从句。然后我们把一些代码包裹进一个```except```从句，它会在```try```从句中的代码触发异常时执行。

在下面的例子中，我们还会使用第三个从句，那就是```finally```从句。包裹到```finally```从句中的代码不管异常是否触发都将会被执行。这可以被用来在脚本执行之后做清理工作。这里是个简单的例子：

```python
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# Output: An IOError occurred. No such file or directory
# This would be printed whether or not an exception occurred!
```