# 调试（Debugging）

调试也是一种你一经掌握，能大大提高你的bug捕捉技术。大部分新人忽略了Python debugger(```pdb```)的重要性。 在这个章节我会只告诉你一些重要的命令。你可以从官方文档中学习到更多。

### 从命令行运行

你可以使用Python debugger从命令行运行一段脚本， 举个例子：
```
$ python -m pdb my_script.py
```
这会触发debugger在它找到的第一行指令处停止执行。这在你的脚本很短时会很有帮助。你可以接着查看变量信息，并且逐行继续执行。

### 从脚本内部运行

你可以在脚本内部设置断点，这样你可以在某些特定点查看变量信息和各种执行时信息。这可以用```pdb.set_trace()```方法来实现。举个例子：
```
import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())
```

Try running the above script after saving it. You would enter the debugger as soon as you run it. Now it’s time to learn some of the commands of the debugger.

Commands:

c: continue execution
w: shows the context of the current line it is executing.
a: print the argument list of the current function
s: Execute the current line and stop at the first possible occasion.
n: Continue execution until the next line in the current function is reached or it returns.
The difference between next and step is that step stops inside a called function, while next executes called functions at (nearly) full speed, only stopping at the next line in the current function.

These are just a few commands. pdb also supports post mortem. It is also a really handy function. I would highly suggest you to look at the official documentation and learn more about it.