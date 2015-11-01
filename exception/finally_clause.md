# finally从句

We wrap our main code in the try clause. After that we wrap some code in an except clause which gets executed if an exception occurs in the code wrapped in the try clause. In this example we will use a third clause as well which is the finally clause. The code which is wrapped in the finally clause will run whether or not an exception occurred. It might be used to perform clean-up after a script. Here is a simple example:

try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# Output: An IOError occurred. No such file or directory
# This would be printed whether or not an exception occurred!
