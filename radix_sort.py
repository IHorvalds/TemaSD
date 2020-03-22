from tests import test
from timsort import tim_sort
from pprint import pprint
from math import log

def radix_sort(arr, *args, radix=2**4):
    if not arr:
        return []
    max_val = max(arr)
    iterations = int(log(max_val, radix)) + 1
    digits = [[] for _ in range(radix)]
    for power in range(1, iterations + 1):
        digit = radix**power
        for i in arr:
            index = (i%digit)//(digit//radix)
            digits[index].append(i)
        arr = []
        for i in range(len(digits)):
            if digits[i]:
                arr += digits[i]
                digits[i] = []
    
    return arr

if __name__ == "__main__":
    test(radix_sort, 10**6, 10**6)
    # test(radix_sort, 20, 56)