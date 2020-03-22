from tests import test
from random import randint

def choose_pivot(v):
	index = randint(0, len(v) - 1)
	return v[index]

def quick_sort(v, *args):
	if not v:
		return []

	pivot = choose_pivot(v)


	lt = []
	eq = []
	hi = []

	for i in v:
		if i < pivot:
			lt.append(i)
		elif i == pivot:
			eq.append(i)
		else:
			hi.append(i)
	return quick_sort(lt)+eq+quick_sort(hi)

if __name__ == "__main__":
	test(quick_sort, 10**6, 10**4)
