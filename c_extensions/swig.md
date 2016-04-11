# SWIG

SWIG是Simplified Wrapper and Interface Generator的缩写。是Python中调用C代码的另一种方法。在这个方法中，开发人员必须编写一个额外的接口文件来作为SWIG(终端工具)的入口。

Python开发者一般不会采用这种方法，因为大多数情况它会带来不必要的复杂。而当你有一个C/C++代码库需要被多种语言调用时，这将是个非常不错的选择。

示例如下(来自[SWIG官网](http://www.swig.org/tutorial.html))

```example.c```文件中的C代码包含了不同的变量和函数
```C
#include <time.h>
double My_variable = 3.0;

int fact(int n) {
    if (n <= 1) return 1;
    else return n*fact(n-1);

}

int my_mod(int x, int y) {
    return (x%y);

}

char *get_time()
{
    time_t ltime;
    time(&ltime);
    return ctime(&ltime);

}
```

编译它
```Shell
unix % swig -python example.i
unix % gcc -c example.c example_wrap.c \
    -I/usr/local/include/python2.1
unix % ld -shared example.o example_wrap.o -o _example.so

```

最后，Python的输出
```Python
>>> import example
>>> example.fact(5)
120
>>> example.my_mod(7,3)
1
>>> example.get_time()
'Sun Feb 11 23:01:07 1996'
>>>
```

我们可以看到，使用SWIG确实达到了同样的效果，虽然下了更多的工夫，但如果你的目标是多语言还是很值得的。
