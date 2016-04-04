from functools import wraps

def a_new_decorator(a_func):
	@wraps(a_func)
	def wrap_the_function():
		print 'I am doing some boring work before executing a_func()'
		a_func()
		print 'I am doing some boring work after executing a_func()'
	return wrap_the_function

@a_new_decorator
def a_function_requiring_decoration():
	'''Hey you! Decorate me!'''
	print 'I am the function which needs some decoration to remove my foul smell'
	

a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
print a_function_requiring_decoration.__name__

