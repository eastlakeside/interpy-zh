# Map

`Map`会将一个函数映射到一个输入列表的所有元素上。这是它的

applies a function to all the items in an input_list. Here is the blueprint:

Blueprint

map(function_to_apply, list_of_inputs)
Most of the times we want to pass all the list elements to a function one-by-one and then collect the output. For instance:

items = [1, 2, 3, 4, 5]
squared = []
for i in items:
    squared.append(i**2)
Map allows us to implement this in a much simpler and nicer way. Here you go:

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
Most of the times we use lambdas with map so I did the same. Instead of a list of inputs we can even have a list of functions!

def multiply(x):
        return (x*x)
def add(x):
        return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# Output:
# [0, 0]
# [1, 2]
# [4, 4]
# [9, 6]
# [16, 8]
