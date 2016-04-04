def file_exception1():
	try:
	    file = open('test.txt', 'rb')
	except EOFError as e:
	    print("An EOF error occurred.")
	    raise e
	except IOError as e:
		print("An error occurred.")
		raise e
	else:
		...
	finally:
		...

def file_exception2():
	try:
		file = open('test.txt', 'rb')
	except (IOError, EOFError) as e:
		print 'An error occurd. {}'.format(e.args[-1])
	finally:
		...

def file_exception3():
	try:
		file = open('test.txt', 'rb')
	except Exception:
		raise
