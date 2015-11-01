# 异常

异常处理是一种艺术，一旦你掌握，会授予你无穷的力量。

Exception handling is an art which once you master grants you immense powers. I am going to show you some of the ways in which we can handle exceptions.

In basic terminology we are aware of try/except clause. The code which can cause an exception to occur is put in the try block and the handling of the exception is implemented in the except block. Here is a simple example:

try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
In the above example we are handling only the IOError exception. What most beginners do not know is that we can handle multiple exceptions.