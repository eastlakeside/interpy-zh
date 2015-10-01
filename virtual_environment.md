# 虚拟环境(virtualenv)
## 你听说过```virtualenv```吗？
如果你是一位初学者，你可能没有听说过```virtualenv```；但如果你是位经验丰富的程序员，那么它可能是你的工具集的重要组织部分。

## 那么，什么是virtualenv?
```Virtualenv``` 是一个工具，它能够帮我们创建一个独立(隔离)的Python环境。想象你有一个应用程序，依赖于版本为2的第三方模块，但另一个程序依赖的版本是3，请问你如何使用和开发这些应用程序？

如果你把一切都安装到了```/usr/lib/python2.7/site-packages```（或者其它平台的标准位置），那很容易出现某个模块被升级而你却不知道的情况。

在另一种情况下，想象你有一个已经开发完成的程序，但是你不想更新它所依赖的第三方模块版本；但你已经开始另一个程序，需要这些第三方模块的版本。


## 用什么方式解决？
使用```virtualenv```！针对每个程序创建独立（隔离）的Python环境，而不是在全局安装所依赖的模块。

要安装它，只需要在命令行中输入以下命令：

```
$ pip install virtualenv
```

最重要的命令是：

```
$ virtualenv myproject
$ source bin/activate
```
执行第一个命令在```myproject```文件夹创建一个隔离的virtualenv环境，第二个命令激活这个隔离的环境(```virtualenv```)。

在创建virtualenv时，你必须做出决定：这个virtualenv是使用系统全局的模块呢？还是只使用这个virtualenv内的模块。
默认情况下，virtualenv不会使用系统全局模块。

如果你想让你的virtualenv使用系统全局模块，请使用```--system-site-packages```参数创建你的virtualenv，例如：

```
virtualenv --system-site-packages mycoolproject
```
使用以下命令可以退出这个virtualenv:

```
$ deactivate
```
Running python after deactivating will use your system installation of Python again.

Bonus

You can use smartcd which is a library for bash and zsh and allows you to alter your bash (or zsh) environment as you cd. It can be really helpful to activate and deactivate a virtualenv when you change directories. I have used it quite a lot and love it. You can read more about it on GitHub

This was just a short intro to virtualenv. There's a lot more to it; this link has more information.