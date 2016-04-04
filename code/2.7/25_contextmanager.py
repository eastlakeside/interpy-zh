class File(object):
	def __init__(self, file_name, method):
		self.file_obj = open(file_name, method)
	def __enter__(self):
		return self.file_obj
	def __exit__(self, type, value, traceback):
		# handle exception
		print 'Exception has been handled'
		self.file_obj.close()
		return True

def main():
	with File('demo.txt', 'w') as opened_file:
		opened_file.write('Hola!')

if __name__ == '__main__':
	main()
