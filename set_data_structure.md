# 5. set Data Structure
set is a really useful data structure. sets behave mostly like lists with the distinction that they can not contain duplicate values. It is really useful in a lot of cases. For instance you might want to check whether there are duplicates in a list or not. You have two options. The first one involves using a for loop. Something like this:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
# Output: ['b', 'n']
But there is a simpler and more elegant solution involving sets. You can simply do something like this:

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = set([x for x in some_list if some_list.count(x) > 1])
print(duplicates)
# Output: set(['b', 'n'])
Sets also have a few other methods. Below are some of them.

Intersection

You can intersect two sets. For instance:

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.intersection(valid))
# Output: set(['red'])
Difference

You can find the invalid values in the above example using the difference method. For example:

valid = set(['yellow', 'red', 'blue', 'green', 'black'])
input_set = set(['red', 'brown'])
print(input_set.difference(valid))
# Output: set(['brown'])
You can also create sets using the new notation:

a_set = {'red', 'blue', 'green'}
print(type(a_set))
# Output: <type 'set'>
There are a few other methods as well. I would recommend visiting the official documentation and giving it a quick read.

Next  Previous
