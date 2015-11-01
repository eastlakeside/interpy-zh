# `open`函数

[open](http://docs.python.org/dev/library/functions.html#open) 可以打开一个文件。超级简单吧？大多数时候，我们看到它这样被使用：
```python
f = open('photo.jpg', 'r+')
jpgdata = f.read()
f.close()
```

我现在写这篇文章的原因，是大部分时间我看到open被这样使用。有**三个**错误存在于上面的代码中。你能把它们全指出来吗？如不能，请读下去。在这篇文章的结尾，你会知道上面的代码错在哪里，而且，更重要的是，你能在自己的代码里避免这些错误。现在我们从基础开始：

open的返回值是一个文件句柄，从操作系传给你的Python程序。一旦你处理完文件，你会想要归还这个文件句柄，只有这样你的程序不会超出一次能打开的文件句柄的数量上限。



The return value from open is a file handle, given out from the operating system to your Python application. You will want to return this file handle once you’re finished with the file, if only so that your application won’t reach the limit of the number of open file handles it can have at once.

Explicitly calling close closes the file handle, but only if the read was successful. If there is any error just after f = open(...), f.close() will not be called (depending on the Python interpreter, the file handle may still be returned, but that’s another story). To make sure that the file gets closed whether an exception occurs or not, pack it into a with statement:

with open('photo.jpg', 'r+') as f:
    jpgdata = f.read()
The first argument of open is the filename. The second one (the mode) determines how the file gets opened.

If you want to read the file, pass in r
If you want to read and write the file, pass in r+
If you want to overwrite the file, pass in w
If you want to append to the file, pass in a
While there are a couple of other valid mode strings, chances are you won’t ever use them. The mode matters not only because it changes the behavior, but also because it may result in permission errors. For example, if we were to open a jpg-file in a write-protected directory, open(.., 'r+') would fail. The mode can contain one further character; we can open the file in binary (you’ll get a string of bytes) or text mode (a string of characters).

In general, if the format is written by humans, it tends to be text mode. jpg image files are not generally written by humans (and are indeed not readable by humans), and you should therefore open them in binary mode by adding a b to the mode string (if you’re following the opening example, the correct mode would be rb). If you open something in text mode (i.e. add a t, or nothing apart from r/r+/w/a), you must also know which encoding to use. For a computer, all files are just bytes, not characters.

Unfortunately, open does not allow explicit encoding specification in Python 2.x. However, the function io.open is available in both Python 2.x and 3.x (where it is an alias of open), and does the right thing. You can pass in the encoding with the encoding keyword. If you don’t pass in any encoding, a system – and Python – specific default will be picked. You may be tempted to rely on these defaults, but the defaults are often wrong, or the default encoding cannot actually express all characters in the file (this will happen often on Python 2.x and/or Windows). So go ahead and pick an encoding. utf-8 is a terrific one. When you write a file, you can just pick the encoding to your liking (or the liking of the program that will eventually read your file).

How do you find out which encoding a file you’re reading was written in? Well, unfortunately, there is no foolproof way to detect the encoding - the same bytes can represent different, but equally valid characters in different encodings. Therefore, you must rely on metadata (for example, in HTTP headers) to know the encoding. Increasingly, formats just define the encoding to be UTF-8.

Armed with this knowledge, let’s write a program that reads a file, determines whether it’s JPG (hint: These files start with the bytes FF D8), and writes a text file that describe the input file.

import io

with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))
I am sure that now you will use open correctly!