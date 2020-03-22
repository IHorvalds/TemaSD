from tests import test

def count_sort(v, *args):
    if not v: # if the array is empty
        return v
    
    max_val = max(v)
    freq = [0] * (max_val + 1)
    sorted_array = []

    for i in v:
        freq[i] += 1

    for value, _ in enumerate(freq):
        while freq[value]:
            sorted_array.append(value)
            freq[value] -= 1
    return sorted_array

if __name__ == "__main__":
    test(count_sort, 10**6, 10**7)
    # test(sorted, 10**6, 10**4)