# 虚拟环境\(virtualenv\)

## 你听说过`virtualenv`吗？

如果你是一位初学者，你可能没有听说过`virtualenv`；但如果你是位经验丰富的程序员，那么它可能是你的工具集的重要组织部分。

## 那么，什么是`virtualenv`?

`Virtualenv` 是一个工具，它能够帮我们创建一个独立\(隔离\)的Python环境。想象你有一个应用程序，依赖于版本为2的第三方模块，但另一个程序依赖的版本是3，请问你如何使用和开发这些应用程序？

如果你把一切都安装到了`/usr/lib/python2.7/site-packages`（或者其它平台的标准位置），那很容易出现某个模块被升级而你却不知道的情况。

在另一种情况下，想象你有一个已经开发完成的程序，但是你不想更新它所依赖的第三方模块版本；但你已经开始另一个程序，需要这些第三方模块的版本。

## 用什么方式解决？

使用`virtualenv`！针对每个程序创建独立（隔离）的Python环境，而不是在全局安装所依赖的模块。

要安装它，只需要在命令行中输入以下命令：

```sh
$ pip install virtualenv
```

最重要的命令是：

```sh
$ virtualenv myproject
$ source myproject/bin/activate
```

执行第一个命令在`myproject`文件夹创建一个隔离的virtualenv环境，第二个命令激活这个隔离的环境\(`virtualenv`\)。

在创建virtualenv时，你必须做出决定：这个virtualenv是使用系统全局的模块呢？还是只使用这个virtualenv内的模块。  
默认情况下，virtualenv不会使用系统全局模块。

如果你想让你的virtualenv使用系统全局模块，请使用`--system-site-packages`参数创建你的virtualenv，例如：

```sh
virtualenv --system-site-packages mycoolproject
```

使用以下命令可以退出这个virtualenv:

```sh
$ deactivate
```

运行之后将恢复使用你系统全局的Python模块。

# 福利

你可以使用`smartcd`来帮助你管理你的环境，当你切换目录时，它可以帮助你激活（activate）和退出（deactivate）你的virtualenv。我已经用了很多次，很喜欢它。你可以在github\([https://github.com/cxreg/smartcd](https://github.com/cxreg/smartcd)\) 上找到更多关于它的资料。

这只是一个virtualenv的简短介绍，你可以在 [http://docs.python-guide.org/en/latest/dev/virtualenvs/](http://docs.python-guide.org/en/latest/dev/virtualenvs/) 找到更多信息。

