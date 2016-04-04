from ctypes import *

def main():
	adder = CDLL('./adder.so')

	res_int = adder.add_int(4,5)
	print 'Sum of 4 and 5 = ', str(res_int)

	a = c_float(5.5)
	b = c_float(4.1)

	add_float = adder.add_float
	add_float.restype = c_float
	print 'Sum of 5.5 and 4.1 = ', str(add_float(a,b))

if __name__ == '__main__':
	main()
