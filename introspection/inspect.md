# inspect模块

The inspect module also provides several useful functions to get information about live objects. For example you can check the members of an object by running:

import inspect
print(inspect.getmembers(str))
# Output: [('__add__', <slot wrapper '__add__' of ... ...
There are a couple of other methods as well which help in introspection. You can explore them if you wish.