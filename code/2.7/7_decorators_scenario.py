from functools import wraps

# 1. Authorization
def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authrization
		if not auth or not check_auth(auth.username, auth.password):
			authenticate()
		return f(*args, **kwargs)
	return decorated

# 2.logging
def logit(func):
	@wraps(func)
	def with_logging(*args, **kwargs):
		print func.__name__ + ' was called'
		return func(*args, **kwargs)
	return with_logging

@logit
def addition_func(x):
	'''Do some math.'''
	return x + x

