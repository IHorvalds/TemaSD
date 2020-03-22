from random import randint
from time import time

def correctly_sorted(v, nr_of_elements):
	if len(v) != nr_of_elements:
		print(len(v), nr_of_elements)
		return False


	for i in range(len(v)-1):
		if(v[i] > v[i+1]):
			print(sorted(v)[i:i+2])
			print(v[i:i+2])
			return False
	return True

def gen_list(nr_of_elements, max_element):
	return list(randint(0, max_element) for _ in range(nr_of_elements))

def time_sort_function(f: callable, array_to_sort, nr_of_elements, *args):
	print(f.__name__)
	init_time = time()
	v = f(array_to_sort, *args)
	print("Time elapsed:", (time() - init_time) * 1000, "ms")
	print("Array corectly sorted" if correctly_sorted(v, nr_of_elements) else "Array sorted incorrectly")

def test(sort_function, nr_of_elements, max_element, *args):

	print("Generating random array...")
	array_to_sort = gen_list(nr_of_elements, max_element)
	print("Generated")

	if isinstance(sort_function, list):
		for f in sort_function:
			if (f.__name__ in ["bubble_sort", "insert_sort"]) and nr_of_elements >= 10**6:
				print("Prea multe elemente pentru ", f.__name__)
				pass
			elif f.__name__ == "count_sort" and max_element >= 10**11:
				print("Element maxim prea mare pentru count sort")
				pass
			else:
				time_sort_function(f, array_to_sort, nr_of_elements, *args)
	else:
		time_sort_function(sort_function, array_to_sort, nr_of_elements, *args)

		
