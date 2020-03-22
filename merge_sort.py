from tests import test

def merge_arrays(arr, low, mid, high):
    l = low
    m = mid
    merged_array = []
    while l < mid and m < high:
        if arr[l] <= arr[m]:
            merged_array.append(arr[l])
            l += 1
        else:
            merged_array.append(arr[m])
            m += 1
    if l == mid:
        merged_array += arr[m : high]
    else:
        merged_array += arr[l : mid]

    arr[low : high] = merged_array


def merge_sort(arr, low, high):
    arr_len = high - low

    if arr_len <= 1:
        return arr

    mid = (low+high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid, high)

    merge_arrays(arr, low, mid, high)
    return arr

if __name__ == "__main__":
    test(merge_sort, 10**6, 10**4, 0, 10**6)