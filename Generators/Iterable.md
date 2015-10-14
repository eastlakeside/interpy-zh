# 可迭代对象(Iterable)

An iterable is any object in Python which has an __iter__ or a __getitem__ method defined which returns an iterator or can take indexes (Both of these dunder methods are fully explained in a previous chapter). In short an iterable is any object which can provide us with an iterator. So what is an iterator?

一个可迭代对象是Python中任意的对象，只要它定义了可以返回一个迭代器的__iter__方法，或者定义了可以支持下标索引的__getitem__方法(这些双下划线方法会在其他章节中全面解释)。简单说，一个可迭代对象，就是任意的对象，只要它能给我们提供一个迭代器。那问题是一个迭代器呢？
