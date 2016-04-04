def fibon(n):
	a = b = 1
	for i in range(n):
		yield a
		a, b = b, a + b

def fibonacci():
	for x in fibon(1000000):
		print x

def generator_function():
	for i in range(3):
		yield i

def main():
	fibonacci()

if __name__ == '__main__':
	main()
