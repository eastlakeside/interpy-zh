# 虚拟环境(virtualenv)
## 你听说过virtualenv吗？
如果你是一位初学者，你可能没有听说过virtualenv；但如果你是位经验丰富的程序员，那么它可能是你的工具集的重要组织部分。

## 那么，什么是virtualenv?
Virtualenv 是一个工具，它能够帮我们创建一个独立(隔离)的Python环境。想象你有一个应用程序，依赖于版本为2的第三方模块，但另一个程序依赖的版本是3，请问你如何使用和开发这些应用程序？

If you install everything into /usr/lib/python2.7/site-packages (or whatever your platform's standard location is), it's easy to end up in a situation where you unintentionally upgrade a package.

In another case, imagine that you have an application which is fully developed and you do not want to make any change to the libraries it is using but at the same time you start developing another application which requires the updated versions of those libraries.

What will you do? Use virtualenv! It creates isolated environments for your python application and allows you to install Python libraries in that isolated environment instead of installing them globally.

To install it, just type this command in the shell:

$ pip install virtualenv
The most important commands are:

$ virtualenv myproject
$ source bin/activate
This first one makes an isolated virtualenv environment in the myproject folder and the second command activates that isolated environment.

While creating the virtualenv you have to make a decision. Do you want this virtualenv to use packages from your system site-packages or install them in the virtualenv’s site-packages? By default, virtualenv will not give access to the global site-packages.

If you want your virtualenv to have access to your systems site-packages, use the --system-site-packages switch when creating your virtualenv like this:

$ virtualenv --system-site-packages mycoolproject
You can turn off the env by typing:

$ deactivate
Running python after deactivating will use your system installation of Python again.

Bonus

You can use smartcd which is a library for bash and zsh and allows you to alter your bash (or zsh) environment as you cd. It can be really helpful to activate and deactivate a virtualenv when you change directories. I have used it quite a lot and love it. You can read more about it on GitHub

This was just a short intro to virtualenv. There's a lot more to it; this link has more information.