# 虚拟环境(virtualenv)
Have you ever heard of virtualenv? If you are a beginner, then you might not have heard about it but if you are a seasoned programmer then it may well be a vital part of your toolset.

So what is virtualenv? Virtualenv is a tool which allows us to make isolated python environments. Imagine you have an application that needs version 2 of a library, but another application requires version 3. How can you use and develop both these applications?

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