# coding=utf-8

# 书中代码 map,filter 前面的list是多余的，因为map本来就会返回一个list

def square():
	items = [1,2,3,4,5]
	print map(lambda x: x**2, items)

def multiply(x):
	return x*x

def add(x):
	return x+x

def filter_less_than_zero():
	number_list = range(-5, 5)
	print filter(lambda x: x<0, number_list)

def main():
	square()

	funcs = [multiply, add]
	for i in range(5):
		print map(lambda x: x(i), funcs)

	filter_less_than_zero()

if __name__ == '__main__':
	main()
