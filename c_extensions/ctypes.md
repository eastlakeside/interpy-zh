# CTypes

Python中的[ctypes模块](https://docs.python.org/2/library/ctypes.html)可能是Python调用C方法中最简单的一种。ctypes模块提供了和C语言兼容的数据类型和函数来加载dll文件，因此在调用时不需对源文件做任何的修改。也正是如此奠定了这种方法的简单性。

示例如下

实现两数求和的C代码，保存为```add.c```
```C
//sample C file to add 2 numbers - int and floats

#include <stdio.h>

int add_int(int, int);
float add_float(float, float);

int add_int(int num1, int num2){
    return num1 + num2;

}

float add_float(float num1, float num2){
    return num1 + num2;

}
```

接下来将C文件编译为```.so```文件(windows下为DLL)。下面操作会生成adder.so文件
```Shell
#For Linux
$  gcc -shared -Wl,-soname,adder -o adder.so -fPIC add.c

#For Mac
$ gcc -shared -Wl,-install_name,adder.so -o adder.so -fPIC add.c

```

现在在你的Python代码中来调用它
```Python
from ctypes import *

#load the shared object file
adder = CDLL('./adder.so')

#Find sum of integers
res_int = adder.add_int(4,5)
print "Sum of 4 and 5 = " + str(res_int)

#Find sum of floats
a = c_float(5.5)
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
print "Sum of 5.5 and 4.1 = ", str(add_float(a, b))

```

输出如下
```
Sum of 4 and 5 = 9
Sum of 5.5 and 4.1 =  9.60000038147
```

在这个例子中，C文件是自解释的，它包含两个函数，分别实现了整形求和和浮点型求和。

在Python文件中，一开始先导入ctypes模块，然后使用CDLL函数来加载我们创建的库文件。这样我们就可以通过变量```adder```来使用C类库中的函数了。当```adder.add_int()```被调用时，内部将发起一个对C函数```add_int```的调用。ctypes接口允许我们在调用C函数时使用原生Python中默认的字符串型和整型。

而对于其他类似布尔型和浮点型这样的类型，必须要使用正确的ctype类型才可以。如向```adder.add_float()```函数传参时, 我们要先将Python中的十进制值转化为c_float类型，然后才能传送给C函数。这种方法虽然简单，清晰，但是却很受限。例如，并不能在C中对对象进行操作。
