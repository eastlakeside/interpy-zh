# 函数缓存 (Function caching)

Function caching allows us to cache the return values of a function depending on the arguments. It can save time when an I/O bound function is periodically called with the same arguments. Before Python 3.2 we had to write a custom implementation. In Python 3.2+ there is an lru_cache decorator which allows us to quickly cache and uncache the return values of a function.

函数缓存允许我们将一个函数基于一些参数的返回值缓存起来。它可以节约时间，在一个I/O密集的函数被定期使用相同的参数调用的时候。在Python 3.2版本以前我们只有写一个自定义的数显。在Python 3.2及以后版本，有个lru_cache的装饰器，允许我们将一个函数的返回值快速缓存或取消缓存

我们来看看，在Python 3.2及以后的版本，和之前的版本，分别如何使用它。
