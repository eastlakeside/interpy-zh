import collections, json

colours = (
		('Yasoob', 'Yellow'),
		('Ali', 'Blue'),
		('Arham', 'Green'),
		('Ali', 'Black'),
		('Yasoob', 'Red'),
		('Ahmed', 'Silver'),
)

def defaultdict_test():
	favourite_colours = collections.defaultdict(list)

	for name, colour in colours:
		favourite_colours[name].append(colour)

	print favourite_colours

def defaultdict_keyError():
	tree = lambda: collections.defaultdict(tree)
	some_dict = tree()
	some_dict['colours']['favourite'] = 'yellow'
	print json.dumps(some_dict)

def counter_test():
	favs = collections.Counter(name for name, colour in colours)
	print favs

def deque_test():
	d = collections.deque()
	d.append('1')
	d.append('2')
	d.append('3')
	d.pop()
	print d
	d.popleft()
	print d

def namedtuple_test():
	Animal = collections.namedtuple('Animal', 'name age type')
	perry = Animal(name='perry', age=31, type='cat')
	print perry.name
	print perry[0]
	# perry.age = 21	This is wrong, you can't change it

def main():
	defaultdict_test()
	defaultdict_keyError()
	counter_test()
	deque_test()
	namedtuple_test()


if __name__ == '__main__':
	main()
