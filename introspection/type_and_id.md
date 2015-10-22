# type和id

The type function returns the type of an object. For example:

print(type(''))
# Output: <type 'str'>

print(type([]))
# Output: <type 'list'>

print(type({}))
# Output: <type 'dict'>

print(type(dict))
# Output: <type 'type'>

print(type(3))
# Output: <type 'int'>
id returns the unique ids of various objects. For instance:

name = "Yasoob"
print(id(name))
# Output: 139972439030304