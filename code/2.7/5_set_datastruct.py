def duplicates(some_list):
	return set([x for x in some_list if some_list.count(x) > 1])

def intersect():
	valid = set(['yellow', 'red', 'blue', 'green', 'black'])
	input_set = set(['red', 'brown'])
	print(input_set.intersection(valid))

def difference():
	valid = set(['yellow', 'red', 'blue', 'green', 'black'])
	input_set = set(['red', 'brown'])
	print(input_set.difference(valid))

def main():
	some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
	print duplicates(some_list)
	intersect()
	difference()

if __name__ == '__main__':
	main()
