from functools import wraps

class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)

            with open(self.logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            self.notify()
            
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        pass

class email_logit(logit):
	def __init__(self, email='admin@myproject.com', *args, **kwargs):
		self.email = email
		super(logit, self).__init__(*args, **kwargs)
	def notify(self):
		pass
