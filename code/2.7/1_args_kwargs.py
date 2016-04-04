def test_var_args(f_arg, *argv):
	print 'first normal arg:', f_arg
	for arg in argv:
		print 'another arg though *argv:', arg


def greet_me(**kwargs):
	for key, value in kwargs.items():
		print '{0} == {1}'.format(key, value)

def main():
	test_var_args('yasoob', 'python', 'eggs', 'test')
	greet_me(name='yasoob')

if __name__ == '__main__':
	main()
