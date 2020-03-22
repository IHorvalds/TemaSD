from tests import test
from random import randint

def choose_pivot(v):
	high = v[len(v) - 1]
	mid = v[(0 + len(v) - 1) //2]
	low = v[0]
	if (low <= mid <= high) or (high <= mid <= low):
		return mid
	if (low <= high <= mid) or (mid <= high <= low):
		return v[len(v) - 1]
	return low

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

def choosepivot(v, low, high):
	# index = randint(low, high)
	return v[low], low

def quicksort_inplace(v, low, high):
	if high <= low:
		return v

	pivot, pivot_index = choosepivot(v, low, high)
	l, h = low, high

	while l < h and (l <= pivot_index <= h):
		if v[l] <= pivot <= v[h]:
			if l != pivot_index != h:
				l += 1
				h -= 1
			elif l == pivot_index:
				h -= 1
			elif h == pivot_index:
				l += 1
		elif v[l] >= pivot >= v[h]:
			if v[l] != pivot != v[h]:
				v[l], v[h] = v[h], v[l]
				l += 1
				h -= 1
			elif v[l] == pivot > v[h]:
				if l == pivot_index:
					v[l], v[h] = v[h], v[l]
					pivot_index = h
					l += 1
				else:
					v[l], v[h] = v[h], v[l]
					l += 1
					h -= 1
			elif v[l] > pivot == v[h]:
				if h == pivot_index:
					v[l], v[h] = v[h], v[l]
					pivot_index = l
					h -= 1
				else:
					v[l], v[h] = v[h], v[l]
					l += 1
					h -= 1
		elif v[l] >= pivot <= v[h]:
			if l != pivot_index != h:
				v[l], v[pivot_index] = v[pivot_index], v[l]
				pivot_index = l
				h -= 1
			elif h == pivot_index:
				v[l], v[h] = v[h], v[l]
				pivot_index = l
				h -= 1
		elif v[l] <= pivot >= v[h]:
			if l != pivot_index != h:
				v[h], v[pivot_index] = v[pivot_index], v[h]
				pivot_index = h
				l += 1

	quicksort_inplace(v, low, pivot_index - 1)
	quicksort_inplace(v, pivot_index + 1, high)

	return v

if __name__ == "__main__":
	test(quicksort_inplace, 10**6, 10**6, 0, 10**6-1)
	# "in place" implementation is twice as slow