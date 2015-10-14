# 生成器(Generators)

生成器也是一种迭代器，但是你只能对其迭代一次。这是因为他们并没有把所有的值存在内存中，他们在运行时生成值。你通过遍历来使用它们，要么用一个“for”循环，要么将它们传递给任意可以进行迭代的函数和结构。大多数时候生成器是以函数来实现的。然而，它们并不返回一个值，而是yield(暂且译作“生出”)一个值。这里有个生成器函数的简单例子：
```
def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print(item)

# Output: 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

在这个案例中不是非常有用。生成器最佳应用场景是，计算大量结果集（特别是包含循环的计算），而你不想在同一时间给所有结果集分配内存。许多Python 2标准库里的返回列表的函数，在Python 3里都修改成了返回生成器，因为生成器只需要更少的资源。
下面是一个计算斐波那契数列的生成器：
It is not really useful in this case. Generators are best for calculating large sets of results (particularly calculations involving loops themselves) where you don’t want to allocate the memory for all results at the same time. Many Standard Library functions that return lists in Python 2 have been modified to return generators in Python 3 because generators require fewer resources.

Here is an example generator which calculates fibonacci numbers:

```
# generator version
def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
Now we can use it like this:

for x in fibon(1000000):
    print(x)
```
This way we would not have to worry about it using a lot of resources. However, if we would have implemented it like this:

```
def fibon(n):
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
```
It would have used up all our resources while calculating a large input. We have discussed that we can iterate over generators only once but we haven’t tested it. Before testing it you need to know about one more built-in function of Python, next(). It allows us to access the next element of a sequence. So let’s test out our understanding:

```
def generator_function():
    for i in range(3):
        yield i

gen = generator_function()
print(next(gen))
# Output: 0
print(next(gen))
# Output: 1
print(next(gen))
# Output: 2
print(next(gen))
# Output: Traceback (most recent call last):
#            File "<stdin>", line 1, in <module>
#         StopIteration
```
As we can see that after yielding all the values next() caused a StopIteration error. Basically this error informs us that all the values have been yielded. You might be wondering that why don’t we get this error while using a for loop? Well the answer is simple. The for loop automatically catches this error and stops calling next. Do you know that a few built-in data types in Python also support iteration? Let’s check it out:

```
my_string = "Yasoob"
next(my_string)
# Output: Traceback (most recent call last):
#      File "<stdin>", line 1, in <module>
#    TypeError: str object is not an iterator
```

Well that’s not what we expected. The error says that str is not an iterator. Well it is right! It is an iterable but not an iterator. This means that it supports iteration but we can not directly iterate over it. How can we then iterate over it? It’s time to learn about one more built-in function, iter. It returns an iterator object from an iterable. Here is how we can use it:

```
my_string = "Yasoob"
my_iter = iter(my_string)
next(my_iter)
# Output: 'Y'
```
Now that is much better. I am sure that you loved learning about generators. Do bear it in mind that you can fully grasp this concept only when you use it. Make sure that you follow this pattern and use generators whenever they make sense to you. You won’t be disappointed!
