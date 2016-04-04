# coding=utf-8
# 尽量不要使用 global 来存结果

def add_return(value1, value2):
	return value1 + value2

def add_global(value1, value2):
	global result
	result = value1 + value2

def main():
	print add_return(1,2)
	add_global(5,5)
	print result

if __name__ == '__main__':
	main()
