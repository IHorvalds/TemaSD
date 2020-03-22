from random import randint, shuffle
from time import time

averages = { }

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

def add_time(f_name, time):
	if f_name in averages.keys():
		averages[f_name] += time
	else:
		averages[f_name] = time

def time_sort_function(f, array_to_sort, nr_of_elements, *args):
	# print(f.__name__)
	init_time = time()
	v = f(array_to_sort, *args)
	finish_time = time()
	#print("Time elapsed:", (finish_time - init_time) * 1000, "ms")
	if correctly_sorted(v, nr_of_elements):
		#print("Array corectly sorted")
		add_time(f.__name__, finish_time - init_time)
	# else:
		#print("Array sorted incorrectly")

	shuffle(array_to_sort)
	#print()

def test(sort_function, nr_of_elements, max_element, *args):

	print("Generating random array...")
	array_to_sort = gen_list(nr_of_elements, max_element)
	print("Generated")
	print()

	if isinstance(sort_function, list):
		for f in sort_function:
			if (f.__name__ in ["bubble_sort", "insert_sort"]) and nr_of_elements >= 10**6:
				print("Prea multe elemente pentru ", f.__name__)
				print()
				pass
			elif f.__name__ == "count_sort" and max_element >= 10**11:
				print("Element maxim prea mare pentru count sort")
				print()
				pass
			elif f.__name__ == "quicksort_inplace":
				time_sort_function(f, array_to_sort, nr_of_elements, 0, nr_of_elements-1)
			elif f.__name__ == "sorted":
				time_sort_function(f, array_to_sort, nr_of_elements)
			else:
				time_sort_function(f, array_to_sort, nr_of_elements, *args)
	else:
		time_sort_function(sort_function, array_to_sort, nr_of_elements, *args)

		
