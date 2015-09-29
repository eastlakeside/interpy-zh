# Usage of *args
*args and **kwargs are mostly used in function definitions. *args and **kwargs allow you to pass a variable number of arguments to a function. What variable means here is that you do not know beforehand how many arguments can be passed to your function by the user so in this case you use these two keywords. *args is used to send a non-keyworded variable length argument list to the function. Here’s an example to help you get a clear idea:

```python
def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
```

This produces the following result:

first normal arg: yasoob
another arg through *argv: python
another arg through *argv: eggs
another arg through *argv: test
I hope this cleared away any confusion that you had. So now let’s talk about **kwargs