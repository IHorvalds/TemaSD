from tests import test
from timsort import tim_sort
from pprint import pprint

def radix_sort(arr, *args, radix=10):
    if not arr:
        return []
    max_val = max(arr)
    iterations = 1
    while max_val:
        iterations += 1
        max_val = max_val//radix
    digits = [[] for _ in range(radix)]
    for power in range(1, iterations+1):
        for i in arr:
            digit = radix**power
            index = (i%digit)//(digit//radix)
            digits[index].append(i)
        arr = []
        for d in digits:
            if d:
                arr += d
                d.clear()
    
    return arr

if __name__ == "__main__":
    test(radix_sort, 10**6, 10**4)
    # test(radix_sort, 20, 56)