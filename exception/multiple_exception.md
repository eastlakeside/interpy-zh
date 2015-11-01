# 处理多个异常

We can use three methods to handle multiple exceptions. The first one involves putting all the exceptions which are likely to occur in a tuple. Like so:

try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print("An error occurred. {}".format(e.args[-1]))
Another method is to handle individual exceptions in separate except blocks. We can have as many except blocks as we want. Here is an example:

try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print("An EOF error occurred.")
    raise e
except IOError as e:
    print("An error occurred.")
    raise e
This way if the exception is not handled by the first except block then it may be handled by a following block, or none at all. Now the last method involves trapping ALL exceptions:

try:
    file = open('test.txt', 'rb')
except Exception:
    # Some logging if you want
    raise
This can be helpful when you have no idea about the exceptions which may be thrown by your program.

