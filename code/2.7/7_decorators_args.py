from functools import wraps

def logit(logfile='out.log'):
	def logging_decorator(func):
		@wraps(func)
		def wrapped_function(*args, **kwargs):
			log_string = func.__name__ + ' was called'
			print log_string

			with open(logfile, 'a') as opened_file:
				opened_file.write(log_string + '\n')

			return func(*args, **kwargs)
		return wrapped_function
	return logging_decorator

@logit()
def myfunc1():
	pass

@logit(logfile='func2.log')
def myfunc2():
	pass

def main():
	myfunc1()
	myfunc2()

if __name__ == '__main__':
	main()
