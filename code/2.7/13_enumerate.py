def enum_test():
	my_list = ['apple', 'banana', 'grapes', 'pear']

	for c, v in enumerate(my_list, 1):
		print c, v

def main():
	enum_test()

if __name__ == '__main__':
	main()
