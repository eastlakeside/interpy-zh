from contextlib import contextmanager

@contextmanager
def open_file(name):
	f = open(name, 'w')
	yield f
	f.close()

def main():
	with open_file('some_file') as f:
		f.write('Hola!')
