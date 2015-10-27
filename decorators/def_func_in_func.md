# 在函数中定义函数

刚才那些就是函数的基本知识了。
So those are the basics when it comes to functions. Let’s take your knowledge one step further. In Python we can define functions inside other functions:

def hi(name="yasoob"):
    print("now you are inside the hi() function")

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    print(greet())
    print(welcome())
    print("now you are back in the hi() function")

hi()
#output:now you are inside the hi() function
#       now you are in the greet() function
#       now you are in the welcome() function
#       now you are back in the hi() function

# This shows that whenever you call hi(), greet() and welcome()
# are also called. However the greet() and welcome() functions
# are not available outside the hi() function e.g:

greet()
#outputs: NameError: name 'greet' is not defined
So now we know that we can define functions in other functions. In other words: we can make nested functions. Now you need to learn one more thing, that functions can return functions too.