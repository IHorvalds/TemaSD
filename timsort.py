from tests import test
from merge_sort import merge_arrays

run_size = 4

def insert_sort(v, low, high):
    for i in range(low+1, high):
        t = v[i]
        j = i - 1
        while v[j] > t and j >= low:
            v[j+1] = v[j]
            j -= 1
        v[j+1] = t
    return v[low:high]

def tim_sort(v, *args):
    arr_size = len(v)
    for i in range(0, len(v), run_size):
        insert_sort(v, i, min(i + run_size, arr_size))

    merge_size = run_size
    while merge_size < arr_size:
        for low in range(0, arr_size, 2 * merge_size):
            mid = low + merge_size
            high = min(low + 2 * merge_size, arr_size)
            merge_arrays(v, low, mid, high)
        merge_size *= 2
    return v

if __name__ == "__main__":
    test(tim_sort, 10**6, 10**4)