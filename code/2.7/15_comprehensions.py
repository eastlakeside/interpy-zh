#coding=utf-8

# 推导式包括三种：list comprehension, dict comprehension, set comprehension

def list_comprehension():
	multiples = [i for i in range(30) if i % 3 is 0]
	square = [i*i for i in range(10)]
	print multiples
	print square

def dict_comprehension():
	mcase = {'a':10, 'b':34, 'A':7, 'Z':3}
	mcase_frequency = {k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)  for k in mcase.keys()}
	print mcase_frequency

def set_comprehension():
	square = {x**2 for x in [1,1,2]}
	print square

def main():
	list_comprehension()
	dict_comprehension()
	set_comprehension()

if __name__ == '__main__':
	main()
